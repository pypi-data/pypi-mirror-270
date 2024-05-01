# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 The Regents of the University of California
#
# This file is part of BRAILS.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
# may be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# You should have received a copy of the BSD 3-Clause License along with
# BRAILS. If not, see <http://www.opensource.org/licenses/>.
#
# Contributors:
# Barbaros Cetiner
#
# Last updated:
# 04-19-2024  

import requests
import copy
import json
from shapely.geometry import LineString, Point
from shapely import wkt
from requests.adapters import HTTPAdapter, Retry
from brails.workflow.FootprintHandler import FootprintHandler 

class TransportationElementHandler:
    def __init__(self): 
        self.queryarea = ''
        self.output_files = {'roads':'Roads.geojson'}
        
    def fetch_transportation_elements(self,queryarea):

        def query_generator(bpoly,eltype):
            bbox = bpoly.bounds
            eltype = eltype.lower()
            if eltype=='bridge':
                query = ('https://geo.dot.gov/server/rest/services/Hosted/' + 
                          'National_Bridge_Inventory_DS/FeatureServer/0/query?'+
                          'where=1%3D1&outFields=*'+
                          f"&geometry={bbox[0]}%2C{bbox[1]}%2C{bbox[2]}%2C{bbox[3]}" +
                          '&geometryType=esriGeometryEnvelope&inSR=4326' + 
                          '&spatialRel=esriSpatialRelIntersects&outSR=4326&f=json')
            elif eltype=='tunnel':
                query = ('https://geo.dot.gov/server/rest/services/Hosted/' +
                         'National_Tunnel_Inventory_DS/FeatureServer/0/query?' +
                         'where=1%3D1&outFields=*'
                         f"&geometry={bbox[0]}%2C{bbox[1]}%2C{bbox[2]}%2C{bbox[3]}" + 
                         '&geometryType=esriGeometryEnvelope&inSR=4326' + 
                         '&spatialRel=esriSpatialRelIntersects&outSR=4326&f=json')                    
            elif eltype=='railroad':
                query = ('https://geo.dot.gov/server/rest/services/Hosted/' + 
                         'North_American_Rail_Network_Lines_DS/FeatureServer/0/query?' + 
                          'where=1%3D1&outFields=*'+
                          f"&geometry={bbox[0]}%2C{bbox[1]}%2C{bbox[2]}%2C{bbox[3]}" +
                          '&geometryType=esriGeometryEnvelope&inSR=4326' + 
                          '&spatialRel=esriSpatialRelIntersects&outSR=4326&f=json')                         
            elif eltype=='primary_road':
                query = ('https://tigerweb.geo.census.gov/arcgis/rest/services/' + 
                          'TIGERweb/Transportation/MapServer/2/query?where=&text='+
                          '&outFields=OID,NAME,MTFCC'
                          f"&geometry={bbox[0]}%2C{bbox[1]}%2C{bbox[2]}%2C{bbox[3]}" +
                          '&geometryType=esriGeometryEnvelope&inSR=4326' + 
                          '&spatialRel=esriSpatialRelIntersects&outSR=4326&f=json')                    
            elif eltype=='secondary_road':
                query = ('https://tigerweb.geo.census.gov/arcgis/rest/services/' + 
                          'TIGERweb/Transportation/MapServer/6/query?where=&text='+
                          '&outFields=OID,NAME,MTFCC'
                          f"&geometry={bbox[0]}%2C{bbox[1]}%2C{bbox[2]}%2C{bbox[3]}" +
                          '&geometryType=esriGeometryEnvelope&inSR=4326' + 
                          '&spatialRel=esriSpatialRelIntersects&outSR=4326&f=json')              
            elif eltype=='local_road':
                query = ('https://tigerweb.geo.census.gov/arcgis/rest/services/' + 
                          'TIGERweb/Transportation/MapServer/8/query?where=&text='+
                          '&outFields=OID,NAME,MTFCC'
                          f"&geometry={bbox[0]}%2C{bbox[1]}%2C{bbox[2]}%2C{bbox[3]}" +
                          '&geometryType=esriGeometryEnvelope&inSR=4326' + 
                          '&spatialRel=esriSpatialRelIntersects&outSR=4326&f=json')  
            else:
                raise NotImplementedError('Element type not implemented')
            return query
        
        def get_el_counts(bpoly, eltype: str) -> int:
            # Define a retry stratey for common error codes to use when
            # downloading data:
            s = requests.Session()
            retries = Retry(total=10, 
                            backoff_factor=0.1,
                            status_forcelist=[500, 502, 503, 504])
            s.mount('https://', HTTPAdapter(max_retries=retries))
            
            # Create the query required to get the element counts:
            query = query_generator(bpoly,eltype)
            query.replace('outSR=4326','returnCountOnly=true')
            
            # Download element count using the defined retry strategy:
            r = s.get(query)
            elcount = r.json()['count']
            
            return elcount      
            
        
        def conv2geojson(datalist,eltype,bpoly):
            eltype = eltype.lower()
            geojson = {'type':'FeatureCollection', 
                       "crs": {"type": "name", "properties": 
                               {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
                       'features':[]}
            for item in datalist:
                if eltype in ['bridge','tunnel']:
                    geometry = [item['geometry']['x'],item['geometry']['y']]
                    if bpoly.contains(Point(geometry)):
                        feature = {'type':'Feature',
                                   'properties':{},
                                   'geometry':{'type':'Point',
                                               'coordinates':[]}}
                    else:
                        continue
                else:
                    geometry = item['geometry']['paths']
                    if bpoly.intersects(LineString(geometry[0])):
                        feature = {'type':'Feature',
                                   'properties':{},
                                   'geometry':{'type':'MultiLineString',
                                               'coordinates':[]}}
                    else:
                        continue
                feature['geometry']['coordinates'] = geometry.copy()
                properties = item['attributes']
                for prop in properties:
                    if prop.count('_')>1:
                        propname = prop[:prop.rindex('_')]
                    else:
                        propname = prop
                    feature['properties'][propname] = properties[prop]
                geojson['features'].append(feature)
            return geojson

        def print_el_counts(datalist,eltype):
            nel = len(datalist)
            eltype_print = eltype.replace('_',' ')
            
            if eltype in ['bridge','tunnel']:
                elntype = 'node'
            else:
                elntype = 'edge'
            
            if nel==1:
                suffix = ''
            else:
                suffix = 's'
            
            print(f'Found {nel} {eltype_print} {elntype}{suffix}')

        def write2geojson(bpoly,eltype):
            # Define a retry stratey for common error codes to use when
            # downloading data:
            s = requests.Session()
            retries = Retry(total=10, 
                            backoff_factor=0.1,
                            status_forcelist=[500, 502, 503, 504])
            s.mount('https://', HTTPAdapter(max_retries=retries))
            
            # Download element data using the defined retry strategy:
            query = query_generator(bpoly,eltype)
            r = s.get(query)
            
            # Check to see if the data was successfully downloaded:
            if 'error' in r.text:
                print(f"Data server for {eltype.replace('_',' ')}s is currently unresponsive." +
                         " Please try again later.")
                datalist = []
            else:
                datalist = r.json()['features']
            
            # If road data convert it into GeoJSON format:
            jsonout = conv2geojson(datalist,eltype,bpoly)  
            
            # If not road data convert it into GeoJSON format and write it into
            # a file: 
            if '_road' not in eltype:      
                print_el_counts(jsonout['features'],eltype)
                if len(datalist)!=0:
                    output_filename = f'{eltype.title()}s.geojson'
                    with open(output_filename, 'w') as output_file:
                        json.dump(jsonout, output_file, indent=2)
                else:
                    jsonout = ''
            return jsonout

        def find(s, ch):
            return [i for i, ltr in enumerate(s) if ltr == ch]

        def lstring2xylist(lstring):
            coords = lstring.xy
            coordsout = []
            for i in range(len(coords[0])):
                coordsout.append([coords[0][i],coords[1][i]])    
            return coordsout

        def combine_write_roadjsons(roadjsons,bpoly):
            roadjsons_combined = {'type':'FeatureCollection', 
                       "crs": {"type": "name", "properties": 
                               {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
                       'features':[]}
            rtype = {'primary_road':'P','secondary_road':'S','local_road':'L'}
            for key, roadjson in roadjsons.items(): 
                for item in roadjson['features']:  
                    # Get into the properties and add RTYPE into edge property  
                    item['properties']['RTYPE'] = rtype[key]  
                    # Get into the geometry and intersect it with the bounding polygon:
                    lstring = LineString(item['geometry']['coordinates'][0]) 
                    coords = lstring.intersection(bpoly)
                    # If output is LineString write the intersecting geometry in item and 
                    # append it to the combined the json file:
                    if coords.geom_type=='LineString':
                        coordsout = lstring2xylist(coords)
                        item['geometry']['coordinates'] = [coordsout]  
                        roadjsons_combined['features'].append(item)
                # If not, create multiple copies of the same json for each linestring:
                    else:
                        mlstring_wkt = coords.wkt
                        inds = find(mlstring_wkt,'(')[1:]
                        nedges = len(inds)
                        for i in range(nedges):
                            if i+1!=nedges:
                                edge = wkt.loads('LINESTRING ' + 
                                                 mlstring_wkt[inds[i]:inds[i+1]-2])
                            else:
                                edge = wkt.loads('LINESTRING ' + 
                                                 mlstring_wkt[inds[i]:-1])
                            coordsout = lstring2xylist(edge)  
                            newitem = copy.deepcopy(item)
                            newitem['geometry']['coordinates'] = [coordsout]
                            roadjsons_combined['features'].append(newitem)

            print_el_counts(roadjsons_combined['features'],'road')
            with open('Roads.geojson', 'w') as output_file:
                json.dump(roadjsons_combined, output_file, indent=2)

        def mergeDataList(dataLists):
            merged = dataLists[0]
            for i in range(1,len(dataLists)):
                data = dataLists[i]
                for left, right in zip(merged,data):
                    if left['attributes']['OBJECTID'] != right['attributes']['OBJECTID']:
                        print(("Data downloaded from the National Bridge Inventory")+
                              ("has miss matching OBJECTID between batches.")+ 
                              ("This may be solved by running Brails again"))
                    left['attributes'].update(right['attributes'])
            return merged
       
        self.queryarea = queryarea
        
        # Initialize FootprintHandler:
        fpHandler = FootprintHandler()
        
        # Run FootprintHandler to get the boundary for the entered location:
        if isinstance(queryarea,tuple):
            bpoly,_ = fpHandler._FootprintHandler__bbox2poly(queryarea)
        else:
            bpoly,_,_ = fpHandler._FootprintHandler__fetch_roi(queryarea)   

        # Define supported element types:
        eltypes = ['bridge', 'tunnel', 'railroad', 'primary_road',
                   'secondary_road', 'local_road']
        roadjsons = {'primary_road':[], 'secondary_road':[], 'local_road':[]}
        
        # Write the GeoJSON output for each element:
        for eltype in eltypes:
            if '_road' not in eltype:
                jsonout = write2geojson(bpoly,eltype)
                if jsonout!='':
                   self.output_files[eltype + 's'] = eltype.capitalize() + 's.geojson'
            else:
                print(f"Fetching {eltype.replace('_',' ')}s, may take some time...")
                roadjsons[eltype] = (write2geojson(bpoly,eltype))
        combine_write_roadjsons(roadjsons,bpoly)
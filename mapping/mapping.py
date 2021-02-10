# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Tue Nov  3 13:16:23 2020
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""

import folium
import pandas as pd
import pymongo
import http.server
import socketserver
import webbrowser


#creates mongodatabase and the collections
myclient = pymongo.MongoClient("mongodb+srv://Arthur:102030_art@landminecluster.ia7dg.mongodb.net/test")
mydb = myclient["Land_Mine_Database"]
act = mydb["Land_Mine_Collection"]
data = pd.DataFrame(list(act.find()))

latstart = data['Lat'][0]
lonstart = data['Lon'][0]
fgv = folium.FeatureGroup(name = "mines")
map1 = folium.Map(location = [latstart, lonstart], zoom_start = 20000)
count = 0
total = 0

for index, row in data.iterrows():
    total += 1

if total <= 10:
    size = 6
elif total <= 20:
    size = 5
elif total <= 30:
    size = 4
else:
    size = 3    
    
for index, row in data.iterrows():
    lat = row['Lat']
    lon = row['Lon']
    detonated = row['Detonated']
    
    if detonated == True:
        colo = 'green'
        detona = '(Not Live)'
    elif detonated == False:
        colo = 'red'
        detona = '(Live)'
    else:
        colo = 'orange'
        detona = '(Unknown)'
    
    fgv = folium.FeatureGroup(name = detona + " Mine " + str(count) + "\n at " + lat + " lat and "+ lon + " lon")
    fgv.add_child(folium.CircleMarker(location = (lat, lon), radius = size, fill_opacity = 0.7, popup = "Mine "+ str(count) + " : \nLatitude: "+ str(lat) + " \nLongitude: "+ str(lon) + "\nDetonated: " + str(detonated), fill_color = colo, color = 'black'))
    map1.add_child(fgv)
    count += 1
    
map1.add_child(folium.LayerControl())
map1.save("mines.html") 

webbrowser.open('mines.html', new = 2)

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'mines.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
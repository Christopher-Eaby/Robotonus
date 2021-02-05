# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Wed Nov  4 10:28:15 2020
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""

import tkinter as tk
import webview
import folium
import pandas as pd
from csv import writer
import pymongo

def display():
    myclient = pymongo.MongoClient("mongodb+srv://Arthur:102030_art@landminecluster.ia7dg.mongodb.net/test")
    mydb = myclient["Land_Mine_Database"]
    act = mydb["Land_Mine_Collection"]
    data = pd.DataFrame(list(act.find()))
    
    latstart = data['Lat'][0]
    lonstart = data['Lon'][0]
    fgv = folium.FeatureGroup(name = "mines")
    map1 = folium.Map(location = [latstart, lonstart], zoom_start = 20000)
    
    for index, row in data.iterrows():
        lat = row['Lat']
        lon = row['Lon']
        depth = row['Depth']
        size = row['Size']
        detonated = row['Detonated']
        fgv.add_child(folium.CircleMarker(location = (lat, lon), radius = 4, fill_opacity = 0.7, popup = "Mine: \nDepth: "+ str(depth) + "m" + " \nRadius: "+ str(size) +"m" + "\nDetonated: " + str(detonated), fill_color = 'lime', color = 'grey'))
    
    map1.add_child(fgv)
    map1.add_child(folium.LayerControl())
    map1.save("mines.html") 
    
    webview.create_window('Hello world', 'mines.html')
    webview.start()  
    
def add(lat, lon, depth, size):
    with open('mines.csv', 'a+', newline='') as f:
        csv_writer = writer(f)
        items = [lat, lon, depth, size]
        csv_writer.writerow(items)

gui = tk.Tk()
# sets the title 
gui.title("Mine finder")
# sets the size
gui.geometry("250x300")

var = 0

lbl5 = tk.Label(gui, text = "Latitude", justify = tk.CENTER, padx = 30, pady = 10)
lbl5.grid(row = 0, column = 0)
txt1 = tk.Text(gui, fg = "black", bg = "plum1", height = 1, width = 15)
txt1.grid(row = 0, column = 1)

lbl6 = tk.Label(gui, text = "Longitude", justify = tk.CENTER, padx = 30, pady = 10)
lbl6.grid(row = 1, column = 0)
txt2 = tk.Text(gui, fg = "black", bg = "plum1", height = 1, width = 15)
txt2.grid(row = 1, column = 1)

lbl7 = tk.Label(gui, text = "Depth", justify = tk.CENTER, padx = 30, pady = 10)
lbl7.grid(row = 2, column = 0)
txt3 = tk.Text(gui, fg = "black", bg = "plum1", height = 1, width = 15)
txt3.grid(row = 2, column = 1)

lbl8 = tk.Label(gui, text = "Size", justify = tk.CENTER, padx = 30, pady = 10)
lbl8.grid(row = 3, column = 0)
txt4 = tk.Text(gui, fg = "black", bg = "plum1", height = 1, width = 15)
txt4.grid(row = 3, column = 1)

lbl8 = tk.Label(gui, text = "Armed", justify = tk.CENTER, padx = 30, pady = 10)
lbl8.grid(row = 4, column = 0)
CB9 = tk.Checkbutton(gui, variable=var)
CB9.grid(row=4, column=1)

b1 = tk.Button(gui, text = "Add", height = 2, width = 9, command = lambda : add(float(txt1.get("1.0","end").strip()), float(txt2.get("1.0","end").strip()), float(txt3.get("1.0","end").strip()), float(txt4.get("1.0","end").strip())))
b1.grid(row = 5, column = 0)    

b1 = tk.Button(gui, text = "Display", height = 2, width = 9, command = lambda : display())
b1.grid(row = 5, column = 1)   
    
gui.mainloop() 
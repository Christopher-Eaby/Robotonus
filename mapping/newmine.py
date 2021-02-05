# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Wed Jan 27 10:41:40 2021
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""

from selenium import webdriver 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
import time
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Arthur:102030_art@landminecluster.ia7dg.mongodb.net/test")
mydb = myclient["Land_Mine_Database"]
act = mydb["Land_Mine_Collection"]

def getLocation():
    options = Options()
    options.add_argument("--use--fake-ui-for-media-stream")
    driver = webdriver.Chrome(executable_path = 'chromedriver.exe',options=options) #Edit path of chromedriver accordingly
    timeout = 20
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]') #Replace with any XPath    
    longitude = [x.text for x in longitude]    
    longitude = str(longitude[0])    
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')    
    latitude = [x.text for x in latitude]    
    latitude = str(latitude[0])    
    driver.quit()    
    return (latitude,longitude)

x, y = getLocation()

results = {'Lat' : x, 'Lon' : y, 'Detonated' : False}

act.insert_one(results)
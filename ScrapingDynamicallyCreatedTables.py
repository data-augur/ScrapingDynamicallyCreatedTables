#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:12:11 2018

@author: sarfraz
"""
from selenium import webdriver
import pandas as pd
import sys

#URL from where the tables will be scraped
URL= 'http://www.scstrade.com/stockscreening/SS_CompanySnapShotYR.aspx?symbol=FATIMA'

#define driver as firefox webdriver 
driver = webdriver.Firefox()

#loads the page in firefox
driver.get(URL)

#get the html element at a specific xpath
element = driver.find_element_by_xpath('//form[1]')

#extract the html from that element
element_html=element.get_attribute('innerHTML')
print(element_html);

#Use try except block to extract the tables from html and to catch the exception gracefully if the table doesnot exist 
try:
    #Read all tables in the response into a list of dataframes
    dataframes = pd.read_html(element_html)
    print(dataframes)
    
    #close the browser / webdriver
    driver.close()
    
#Incase no table is found print "No table found" and exit gracefully
except:
    print("No table found")
    
    #close the browser / webdriver
    driver.close()
    
    #exit program
    sys.exit(0)
    

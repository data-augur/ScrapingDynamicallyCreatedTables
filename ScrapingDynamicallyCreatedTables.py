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

#close the browser / webdriver
driver.close()
    

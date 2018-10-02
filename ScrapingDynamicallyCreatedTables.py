#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:12:11 2018

@author: sarfraz
"""
from selenium import webdriver

#URL from where the tables will be scraped
URL= 'http://www.scstrade.com/stockscreening/SS_CompanySnapShotYR.aspx?symbol=FATIMA'

#define driver as firefox webdriver 
driver = webdriver.Firefox()

#make get request for the url that opens the page in firefox
driver.get(URL)



# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 23:49:17 2018

@author: gmallya
"""
# Broad preliminary Goal - This file should be able to fetch prices for hotels in a locality and
# write it to a csv file ("rates.csv"). The prices dumped into this csv file 
# will be either shown as a table or as a plot after doing some data wrangling
 
import requests
from bs4 import BeautifulSoup
import time
import random

with open('rates.csv', 'w') as rates:
    rates.write("Date,Rate\n")
    for m in range(3,4): #range(8,13):
        for d in range(11,32):
            hotel_price = random.randint(1,101)
            # write dummy input into rates.csv
            rates.write("2018-" + str(m) + "-" + str(d) + "," + str(hotel_price) + "\n")
            
#            web_response = requests.get('https://www.tripadvisor.com/Hotels-g37242-Lafayette_Indiana-Hotels.html')
#            if response.ok:
#                soup = BeautifulSoup(web_response.text)
#            # Do not abuse the internet!
#            # time.sleep(1)
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

import numpy as np
import matplotlib.pyplot as plt
import random
###### USER INPUT- Provide the Tripadvisor URL #####
#url = 'https://www.tripadvisor.com/Hotels-g37242-Lafayette_Indiana-Hotels.html'
url = 'https://www.tripadvisor.com/HotelsNear-g60745-qBOS-Boston_Massachusetts.html' 
######################

with open('rates.csv', 'w') as rates:
    # Read HTML content from the url provided by the user
    web_response = requests.get(url)
    
    # Process the content only if the web request was successful
    if web_response.ok:
        # Write the header line to rates.csv file
        rates.write("S.No.; Property Name; Best Price; Booking Website; User Rating; No. of Reviews\n")
        
        # Parse the HTML content using Beautiful Soup        
        soup  = BeautifulSoup(web_response.text,"lxml")
        
        # Read all hotel listings available at the current url
        hotels = soup.findAll('div','listing')
        
        # Loop through each listing to extract relevant details
        ind = 0
        prices = []
        for element in hotels:
            if element.find('a','property_title'):
                ind = ind + 1
                hotel_name = element.find('a','property_title').get_text()
                hotel_rating = element.find('span','ui_bubble_rating')['alt'].replace('bubbles','').strip()
                hotel_review = element.find('a','review_count').get_text().replace('reviews','').strip()
                if element.find('div','price'):
                    hotel_price = element.find('div','price').get_text()
                    if str(hotel_price)=='':
                        prices.append(0)
                        hotel_price = 'NA'
                    else:
                        prices.append(int(hotel_price.replace('$','')))
                    booking_website = element.find('span','provider').get_text()
#                    print '%d, %s, %s, %s, %s, %s' %(ind, hotel_name, hotel_price, booking_website,hotel_rating, hotel_review)
                    rates.write(str(ind) + "; " + hotel_name + "; " + hotel_price + "; " + booking_website + "; " + hotel_rating + "; " + hotel_review + "\n")
                else:
                    prices.append(0)
#                    print '%d, %s, %s, %s, %s, %s' %(ind, hotel_name, 'NA', 'NA',hotel_rating, hotel_review)
                    rates.write(str(ind) + "; " + hotel_name + "; " + "NA" + "; " + "NA" + "; " + hotel_rating + "; " + hotel_review + "\n")
        n, bins, patches = plt.hist(prices, 5, facecolor='g', alpha=0.75)
        plt.xlabel('Hotel Prices')
        plt.ylabel('Frequency')
        plt.title('Histogram of Hotel Prices')
        plt.grid(True)
        txt = "Mean = $%0.1f\nMedian = $%0.1f\nStd = $%0.1f" % (np.mean(prices), np.median(prices), np.std(prices))
        plt.annotate(txt, xy=(0.7, 0.7), xycoords='axes fraction')
        plt.show()
        
#            # Do not abuse the internet!
#            # time.sleep(1)
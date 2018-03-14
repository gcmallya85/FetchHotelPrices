# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:49:49 2018

@author: gmallya
"""

# Broad preliminary Goal - This file should be able to fetch prices for a hotel of users choice
# during user chosen period
# write it to a csv file ("rates_ts.csv"). The prices are dumped into this csv file 
# will be either shown as a table or as a time-series plot after doing some data wrangling
 
import requests
from bs4 import BeautifulSoup
import calendar
import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import timedelta, date

###### USER INPUT- Provide the expedia URL #####
url1 = 'https://www.expedia.com/Indianapolis-Hotels-Ironworks-Hotel-Indy.h19294032.Hotel-Information?adults=2&children=0&chkin='
url2 = '&chkout='
url3 = '&regionId=178266&sort=guestRating&hwrqCacheKey=f86d4beb-550f-4d92-aeac-e5e95630891bHWRQ1520973595877&vip=false&=undefined&exp_dp=169.44&exp_ts=1520973593462&exp_curr=USD&exp_pg=HSR&daysInFuture=&stayLength=&ts=1520973766236'
date_checkin = '03/14/2018'
date_checkout = '04/30/2018'
################################################

##### User defined function to get a list of dates between two dates #####
def daterange(start_date, end_date): #start_date = year(YYYY, MM, DD)
    for dt_frac in range(int ((end_date - start_date).days)+1):
        yield start_date + timedelta(dt_frac)
##########################################################################


#### Get a list of dates between user provided dates of interest #####        
M1 = int(date_checkin[0:2])
D1 = int(date_checkin[3:5])
Y1 = int(date_checkin[6:10])

M2 = int(date_checkout[0:2])
D2 = int(date_checkout[3:5])
Y2 = int(date_checkout[6:10])

start_dt = date(Y1, M1, D1)
end_dt = date(Y2, M2, D2)
dt_list = []
for dt in daterange(start_dt, end_dt):
    dt_list.append(dt.strftime("%m/%d/%Y").replace('/','%2F'))
#######################################################################

web_response_ind = 0
with open('rates_ts.csv', 'w') as rates:
    for n in range(len(dt_list)):
        url1 = 'https://www.expedia.com/Indianapolis-Hotels-Ironworks-Hotel-Indy.h19294032.Hotel-Information?adults=2&children=0&chkin='
        url2 = '&chkout='
        url3 = '&regionId=178266&sort=guestRating&hwrqCacheKey=f86d4beb-550f-4d92-aeac-e5e95630891bHWRQ1520973595877&vip=false&=undefined&exp_dp=169.44&exp_ts=1520973593462&exp_curr=USD&exp_pg=HSR&daysInFuture=&stayLength=&ts=1520973766236'
        if n < len(dt_list)-1:
            url = url1 + dt_list[n] + url2 + dt_list[n+1] + url3
            # Read HTML content from the url provided by the user
            web_response = requests.get(url)
                    
            # Process the content only if the web request was successful
            if web_response.ok:
                web_response_ind = web_response_ind + 1
                print '%d\n' % (web_response_ind)
                # Write the header line to rates.csv file
                rates.write("Check in date; Price\n")
                
                # Parse the HTML content using Beautiful Soup        
                soup  = BeautifulSoup(web_response.text,"lxml")
                
                # Read all room listings available at the current url
                hotels = soup.findAll('h3','room-name')
    #            
    #            # Loop through each listing to extract relevant details
    #            ind = 0
    #            prices = []
    #            for element in hotels:
    #                if element.find('a','property_title'):
    #                    ind = ind + 1
    #                    hotel_name = element.find('a','property_title').get_text()
    #                    hotel_rating = element.find('span','ui_bubble_rating')['alt'].replace('bubbles','').strip()
    #                    hotel_review = element.find('a','review_count').get_text().replace('reviews','').strip()
    #                    if element.find('div','price'):
    #                        hotel_price = element.find('div','price').get_text()
    #                        if str(hotel_price)=='':
    #                            prices.append(0)
    #                            hotel_price = 'NA'
    #                        else:
    #                            prices.append(int(hotel_price.replace('$','')))
    #                        booking_website = element.find('span','provider').get_text()
    #    #                    print '%d, %s, %s, %s, %s, %s' %(ind, hotel_name, hotel_price, booking_website,hotel_rating, hotel_review)
    #                        rates.write(str(ind) + "; " + hotel_name + "; " + hotel_price + "; " + booking_website + "; " + hotel_rating + "; " + hotel_review + "\n")
    #                    else:
    #                        prices.append(0)
    #    #                    print '%d, %s, %s, %s, %s, %s' %(ind, hotel_name, 'NA', 'NA',hotel_rating, hotel_review)
    #                        rates.write(str(ind) + "; " + hotel_name + "; " + "NA" + "; " + "NA" + "; " + hotel_rating + "; " + hotel_review + "\n")
    #            n, bins, patches = plt.hist(prices, 5, facecolor='g', alpha=0.75)
    #            plt.xlabel('Hotel Prices')
    #            plt.ylabel('Frequency')
    #            plt.title('Histogram of Hotel Prices')
    #            plt.grid(True)
    #            txt = "Mean = $%0.1f\nMedian = $%0.1f\nStd = $%0.1f" % (np.mean(prices), np.median(prices), np.std(prices))
    #            plt.annotate(txt, xy=(0.7, 0.7), xycoords='axes fraction')
    #            plt.show()
    #            
    #    #            # Do not abuse the internet!
    #    #            # time.sleep(1)
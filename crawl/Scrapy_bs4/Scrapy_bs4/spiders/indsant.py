#import urllib3
#from bs4 import BeautifulSoup
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
#from selenium.common.exceptions import TimeoutException
#import time
#import pandas as pd
#import numpy as np
#lis = []
# path of chromedriver
#chrome_driver_path = "E:/web crawling/crawls/demo_scrapy/demo_scrapy/spiders/chromedriver"
#delay = 15
#driver = webdriver.Chrome(executable_path = chrome_driver_path)
#main_url  = 'https://www.indiasanta.com'
#driver.get(main_url)
#soup = BeautifulSoup(driver.page_source,'html.parser')
#exp = soup.find('ul',{'class':'main_ul_exp'})
#cats = []
#subcats = {}
#ca = exp.find_all('li',{'class':'main_ul_ul col-md-3'})
#for c in ca:
#    cats.append(c.a.text)
#    sca = c.find('div',{'class':'dropdown-submenu'}).find_all('p')
#    #print(sca)
#    sa = []
 #   for s in sca:
        #print(s.text)
#        sa.append(s.a.text)
#    subcats[c.a.text]= sa
#print(cats)
#print(subcats)
#driver.quit()

import datetime
print(datetime.datetime.now())
print('{}-{}'.format(datetime.datetime.now().day,datetime.datetime.now().strftime('%b')))
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd

url = 'https://www.giftbasketsspain.es/birthday_spain.asp'

# path of chromedriver
chrome_driver_path = "E:/web crawling/crawls/demo_scrapy/demo_scrapy/spiders/chromedriver"
delay = 15
driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver.get(url)
rows = []
try:
    WebDriverWait(driver,delay).until(presence_of_all_elements_located((By.CLASS_NAME,'group-product')))
except TimeoutException:
    print('Loading exceeds delay time')
else:
    soup = BeautifulSoup(driver.page_source,'html.parser')
    products = soup.find_all('div',{'class' : 'group-product'})
    #prod = products.find_all('a',{'class':''})
    for prod in products:
        img = prod.a.img['src']
        name = prod.p.get_text()
        rows.append([img,name])

print(rows)
driver.quit()
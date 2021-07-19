#import urllib3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.common.exceptions import TimeoutException
import datetime
import pandas as pd

lis = []
# path of chromedriver
chrome_driver_path = "E:/web crawling/crawls/demo_scrapy/demo_scrapy/spiders/chromedriver"
delay = 15
driver = webdriver.Chrome(executable_path = chrome_driver_path)
main_url  = 'https://www.indiasanta.com'
driver.get(main_url)
soup = BeautifulSoup(driver.page_source,'html.parser')
exp = soup.find('ul',{'class':'main_ul_exp'})
cats = []
subcats = {}
ca = exp.find_all('li',{'class':'main_ul_ul col-md-3'})
for c in ca:
    cats.append(c.a.text)
    sca = c.find('div',{'class':'dropdown-submenu'}).find_all('p')
    #print(sca)
    sa = []
    for s in sca:
        #print(s.text)
        sa.append(s.a.text)
    subcats[c.a.text]= sa
id = 0
print(subcats)
for i in cats:
    for j in subcats[i]: 
        url = 'https://www.indiasanta.com/experience/{}/{}'.format('-'.join(i.split(' ')),'-'.join(j.split(' '))) 
        
        for pg in range(1,50):
            if j == 'Cultural & Spiritual':
                k = 'Cultural-%26-Spiritual'
                page_url = 'https://www.indiasanta.com/Experience/load_data?page={}&price=&cats={}&subcats={}&brand=&age=&forp=&relation=&occasion=&location=&keysearch=&sort_by=&font=&region=&state=&city='.format(pg,'-'.join(i.split(' ')),k)
            else:
                page_url = 'https://www.indiasanta.com/Experience/load_data?page={}&price=&cats={}&subcats={}&brand=&age=&forp=&relation=&occasion=&location=&keysearch=&sort_by=&font=&region=&state=&city='.format(pg,'-'.join(i.split(' ')),'-'.join(j.split(' ')))
            driver.get(page_url)
           
            #try:
            #    WebDriverWait(driver,delay).until(presence_of_all_elements_located((By.CLASS_NAME,'col-sm-4 product-padding')))
            #except TimeoutException:
            #    print('Loading exceeds delay time')
            #else:
            soup = BeautifulSoup(driver.page_source,'html.parser')
            products = soup.find_all('div',{'class' : 'col-sm-4 product-padding'})
            #prod = products.find_all('a',{'class':''})
            print(len(products))
            for prod in products:
                id = id + 1
                h2 = prod.find_all('h2')
                try:
                    price = int(round(float(h2[1].text.strip()[3:])))
                    s_pp = ''
                except ValueError:
                    price = int(round(float(h2[1].text.strip()[2:7].strip())))
                    s_pp = int(round(float(h2[1].text.strip()[14:].strip())))
                
                dets = {
                    'URLink':url,
                    'Date':'{}-{}'.format(datetime.datetime.now().day,datetime.datetime.now().strftime('%b')),
                    'Relation':'',
                    'Occasion':'',
                    'ID':id,
                    'Type':'external',
                    'SKU':'EXP-{}'.format(1000+id),
                    'Name':prod.find('div',{'class':'img'}).h3.a.text.strip(),
                    'Published':1,
                    'Is featured?':0,
                    'Visibility':'visible',
                    'Short description': prod.find('div',{'class':'img'}).h3.a.text.strip(),
                    'Description': '',
                    'Date sale' : '',
                    'Tax status' : '',
                    'Tax class' : '',
                    'In stock?' : 1,
                    'Stock':'',
                    'Low stock':'',
                    'Backorder':0,
                    'Sold individually?':0,
                    'Weight(kg)':'',
                    'Length(cm)' : '',
                    'Width(cm)' : '',
                    'Height(cm)' : '',
                    'Allow customer reviews':0,
                    'Purchase note':'',
                    'Sale price':s_pp,
                    'Regular price':price,
                    'Categories':'-'.join(i.split(' ')),
                    'Tags':'',
                    'Shipping class':'',
                    'Images': prod.find('div',{'class':'img'}).a.img['src'],
                    'Download limit':'',
                    'Download expiry days':'',
                    'Parent':'',
                    'Grouped products':'',
                    'Upsells':'',
                    'Cross-sells':'',
                    'External Url':prod.find('div',{'class':'img'}).h3.a.href,
                    'Button text':'Get it Now',
                    'Location':h2[0].text.strip(),
                    'Attribute 1 name':'Product Type',
                    'Attribute 1 value(s)':'Experienced',
                    'Attribute 1 visible':1,
                    'Attribute 1 global':0
                }
                lis.append(dets)
            if len(products)<18:
                break

df = pd.DataFrame(lis)
df.to_csv('inds_ex4.csv',index=False)
driver.quit()

#page = driver.execute_script("return document.documentElement.outerHTML")
#http = urllib3.PoolManager()

#resp = http.request("GET", url)
#request = urllib3.request("GET",url)#,headers = {"User-Agent":'Chrome/91.0.4472.124'})
#page = urllib3.urlopen(request)

#print(resp.data)
#soup = BeautifulSoup(resp.data,'html.parser')
#soup.find('title')
#for prod in soup.find_all('div',_class = 'col-sm-4 product-padding'):
#    ext_url = prod.find('a').href
#    image = prod.find('img').src
#    print(ext_url)
#    print(image)
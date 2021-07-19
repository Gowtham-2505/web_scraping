# web_scraping
This repository consists of web scrapers which extract data from websites and convert them to csv

When navigated to spiders folder , one can find giftre.py,giftspain.py,indsant2.py<br>
These files are called spiders which crawl over websites and gives us data.

Files which use "scrapy" module:<br>
giftre.py

Files which use "selenium" and "beautifulsoup" module:<br>
giftspain.py,indsant2.py

To run these files use anaconda prompt and activate new conda environment which have modules stated in requirements.txt 

To run a scrapy spider and save data as .csv file:<br>
we have to run :&nbsp;&nbsp;&nbsp;&nbsp;>> scrapy crawl "spider_name" -o data.csv

To run a scrapy spider and save data as .json file:<br>
we have to run :&nbsp;&nbsp;&nbsp;&nbsp;>>scrapy crawl "spider_name" -o data.json

To run a spider which have beautifulsoup and selenium<br>
we have to run :&nbsp;&nbsp;&nbsp;&nbsp;>>python file_name.py

currently scraped sites have only .html powered files and js powered files

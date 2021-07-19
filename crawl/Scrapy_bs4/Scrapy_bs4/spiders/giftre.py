import scrapy
import pandas

class giftreSpider(scrapy.Spider):
    name = 'giftre'   #spider name
    c = 194
    per = 1046
    
    # this is another way to code for inputing website to parser
    #start_urls = ["https://www.giftcart.com/all-gifts/dad.html?p=1"]
    #            "https://www.giftcart.com/all-gifts/boyfriend.html?p=1",
    #            "https://www.giftcart.com/all-gifts/brother.html ",
    #            "https://www.giftcart.com/all-gifts/babies_1.html "]
    def start_requests(self):
        rela = [['dad',25],['brother',31],['teens_1',45],['boyfriend',52],['kids',8],['babies_1',3],['girlfriend',19],['huband',27],['wife',22],['friend',47],['mom',30],['sister',6]]
        urls = []
        for k in range(len(rela)):
            for i in range(rela[k][1]):
                urls.append("https://www.giftcart.com/all-gifts/{}.html".format(rela[k][0])+"?p="+str(i+1))
            for url in urls:
                yield scrapy.Request(url = url,callback = self.parse)
        

    def parse(self,response):
        relation = ''
        url = ''
        try:
            if type(int(response.url.split('/')[-1][-2:])) == int:
                relation = response.url.split('/')[-1][:-10].title()
                url = response.url[:-5]
        except:
            relation = response.url.split('/')[-1][:-9].title()
            url = response.url[:-4]
        
        if relation in ['Babies_1','Teens_1']:
            relation = relation[:-2]
        if relation in ['Babies','Kids']:
            cate = 'Kids'
        elif relation == 'Girlfriend':
            cate = 'Best Friend(Her)'
        elif relation == 'Boyfriend':
            cate = 'Best Friend(Him)'
        else:
            cate = relation
        for prod in response.xpath("//div[@class = 'product-item-info']"):
            price1 = prod.xpath(".//div[@class = 'price-box price-final_price']/span/span/span[contains(@class ,'price-wrapper')]/span[contains(@class,'price')]//text()").extract_first()
            price2 = prod.xpath(".//div[@class = 'price-box price-final_price']/span/span[contains(@class ,'price-wrapper')]/span[contains(@class,'price')]//text()").extract_first()
            link = prod.xpath(".//div[@class = 'name-on-list']/a/@href").extract_first()#+"product.info.description"
            giftreSpider.c = giftreSpider.c + 1
            giftreSpider.per = giftreSpider.per +1
            print(giftreSpider.c)
            if response.xpath(".//div[@class = 'stock unavailable']/span//text()").extract_first() == "Out of stock":
                stock = 0
            else:
                stock = 1
            if price1 == None: 
                yield {
                    'URLink':url,     ## Need to check for pg.nos
                    'Date':'29-Jun',
                    'Relation' : relation,
                    'ID': giftreSpider.c,
                    'Type': 'external',
                    'SKU':'PER-'+str(giftreSpider.per),
                    'Name' : (prod.xpath(".//div[@class = 'name-on-list']/a/text()").extract_first()).strip(),
                    'Published':1,
                    'Is featured?':0,
                    'Visibility in catalog':'visible',
                    'In stock?':stock,
                    'Backorders allowed?':0,
                    'Sold individually?':0,
                    'Allow customer reviews?':0,
                    'Regular price' : int(''.join(price2[1:-3].split(','))),
                    'Categories':cate,
                    'Tags': 'Best Gifts of '+relation,
                    'Images'  : prod.xpath(".//div[@class = 'product-top']/a/img/@data-original").get(),
                    'External URL': link,
                    'Button text':'Get it Now',
                    'Attribute 1 name':'Product Type',
                    'Attribute 1 value(s)':'Personalized',
                    'Attribute 1 visible':1,
                    'Attribute 1 global':0,
                }
            else:
                yield {
                    'URLink':url,
                    'Date':'29-Jun',
                    'Relation' : relation,
                    'ID': giftreSpider.c,
                    'Type': 'external',
                    'SKU':'PER-'+str(giftreSpider.per),
                    'Name' : (prod.xpath(".//div[@class = 'name-on-list']/a/text()").extract_first()).strip(),
                    'Published':1,
                    'Is featured?':0,
                    'Visibility in catalog':'visible',
                    'In stock?':stock,
                    'Backorders allowed?':0,
                    'Sold individually?':0,
                    'Allow customer reviews?':0,
                    'Regular price' : int(''.join(price1[1:-3].split(','))),
                    'Categories':cate,
                    'Tags': 'Best Gifts of '+relation,
                    'Images'  : prod.xpath(".//div[@class = 'product-top']/a/img/@data-original").get(),
                    'External URL':link,
                    'Button text':'Get it Now',
                    'Attribute 1 name':'Product Type',
                    'Attribute 1 value(s)':'Personalized',
                    'Attribute 1 visible':1,
                    'Attribute 1 global':0,                    
                }
        
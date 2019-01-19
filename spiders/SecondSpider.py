# -*- coding: utf-8 -*-

import scrapy
from example.items import NewItem

class SecondSpider(scrapy.Spider):
    name = "SecondSpider"
    
    allowed_domains = ['www.superdatascience.com']
    start_urls = ['https://www.superdatascience.com']    
    def parse(self, response):
        item=NewItem()
        item['main_headline'] = response.xpath('//span/text()').extract()
        item['headline']=response.xpath('//title/text()').extract()
        item['url']=response.url
        item['project']=self.settings.get('BOT_NAME')
        item['spider']=self.name
        return item
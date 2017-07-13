# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse

class CitySpider(scrapy.Spider):
    name = "city"
    start_urls = [
        'http://sz.58.com/nanshan/zufang/0/j2/?minprice=0_1600&PGTID=0d300008-0071-367d-7e8f-38bb92b6eebc&ClickID=2',
        
    ]

    def parse(self, response):
        for info in response.css('li'):
            yield {
                'text':info.css('.des .room')[0].extract(),
			    'author':info.css('.des .add')[0].extract(),
			      
            }     
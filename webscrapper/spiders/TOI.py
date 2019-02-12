# -*- coding: utf-8 -*-
import scrapy


class ToiSpider(scrapy.Spider):
    name = 'TOI'
    allowed_domains = ['https://timesofindia.indiatimes.com/archive.cms']
    start_urls = ['http://https://timesofindia.indiatimes.com/archive.cms/']

    def parse(self, response):
    	lst = []
        for link in response.css('a.normtxt::attr(href)').extract():
        	lst.append(link)
        print lst




        #30 Dec 1899 00:00

        #86400000


        
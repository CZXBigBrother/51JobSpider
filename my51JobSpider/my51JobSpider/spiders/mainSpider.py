# -*- coding: utf-8 -*-
import scrapy
from my51JobSpider.items import My51JobspiderItem

class MainspiderSpider(scrapy.Spider):
    name = 'mainSpider'
    allowed_domains = ['51job.com']
    start_urls = ['http://www.51job.com/']

    def parse(self, response):
        liststype = response.xpath('/html/body/div[5]/div[2]//div//a/@href')
        for url in liststype:
            yield scrapy.Request(url=url.extract(),callback=self.parseSearch)

        pass
    def parseSearch(self,response):
        listsjob = response.xpath('//*[@id="resultList"]//div/p/span/a/@href')
        listpages = response.xpath('//div[@class="p_in"]/ul/li/a/@href')
        for page in listpages:
            yield scrapy.Request(url=page.extract(),callback=self.parseSearch)
        for url in listsjob:
            yield scrapy.Request(url=url.extract(),callback=self.parseDesc)
        pass

    def parseDesc(self,response):
        context= response.text
        title = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/h1/text()').extract()[0]
        area = response.xpath('//span[@class="lname"]/text()').extract()[0]
        money = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/strong/text()').extract()[0]
        exp = response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div/span[1]/text()').extract()[0]
        study = response.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div/div/span[2]/text()').extract()[0]
        all = response.xpath('/html/body/div[3]/div[2]/div[2]/div/div[1]/p[2]/text()').extract()[0]
        lists = all.replace(' ','').replace('\r','').replace('\t','').split('|')
        company = lists[0]
        people = lists[1]
        type = lists[2]

        print (title)
        item = My51JobspiderItem()
        item['title'] = title
        item['area'] = area
        item['money'] = money
        item['company'] = company
        item['people'] = people
        item['type'] = type
        item['study'] = study
        item['exp'] = exp
        yield item
        pass




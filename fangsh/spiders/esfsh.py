# -*- coding: utf-8 -*-
import scrapy
from fangsh.items import FangshItem

class EsfshSpider(scrapy.Spider):
    name = 'esfsh'
    allowed_domains = ['esf.sh.fang.com/']
    start_urls = ['http://esf.sh.fang.com/']

    def parse(self, response):
        base_url = "http://esf.sh.fang.com"
        search_url = response.xpath('//div[@class="screen_al"]/ul/li[@id="list_D02_10"]/ul//li/a/@href').getall()
        for i  in search_url:
            url1= response.urljoin(i)
            # print(url1)
            yield  scrapy.Request(url = url1,callback=self.parse_url, dont_filter=True)
    def parse_url(self,response):
        url_half_lists =response.xpath('//dd/h4/a/@href').getall()

        for url_half in url_half_lists:
            url_full = response.urljoin(url_half)
            # print(url_full)
            yield scrapy.Request(url=url_full,callback=self.parse_detail,dont_filter=True)
        next_page = response.xpath('//div[@id="list_D10_15"]/p[last()-2]/a/@href').get()
        url_next = response.urljoin(next_page)
        yield scrapy.Request(url= url_next,callback=self.parse_url)

    def parse_detail(self,response):
        item = FangshItem()
        # item['ithuxing']    = response.xpath('//div[@class="trl-item1 w146"]/div[@class="tt"]/text()').get().strip()
        # item['chaoxing']  = response.xpath('//div[@class="trl-item1 w146"]/div[@class="tt"]/text()').getall()[1]
        # item['daxiao']    = response.xpath('//div[@class="trl-item1 w182"]/div[@class="tt"]/text()').get().strip()
        # item['louceng']   = response.xpath('//div[@class="trl-item1 w182"]/div[@class="tt"]/text()').get()[1]
        # item['danjia ']   = response.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]/text()').get().strip()
        # item['zhuangxiu'] = response.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]/text()').get()[1]
        # item['jiage']    = response.xpath('//div[@class="trl-item price_esf  sty1"]/i/text()').get()
        huxing   = response.xpath('//div[@class="trl-item1 w146"]/div[@class="tt"]/text()').get().strip()
        chaoxing = response.xpath('//div[@class="trl-item1 w146"]/div[@class="tt"]/text()').getall()[1]
        daxiao    = response.xpath('//div[@class="trl-item1 w182"]/div[@class="tt"]/text()').get().strip()
        louceng  = response.xpath('//div[@class="trl-item1 w182"]/div[@class="tt"]/text()').get()[1]
        danjia   = response.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]/text()').get().strip()
        zhuangxiu = response.xpath('//div[@class="trl-item1 w132"]/div[@class="tt"]/text()').getall()[1]
        jiage  = response.xpath('//div[@class="trl-item price_esf  sty1"]/i/text()').get()
        print(huxing,chaoxing,daxiao,louceng,danjia,zhuangxiu,jiage,sep= "++++++++++")















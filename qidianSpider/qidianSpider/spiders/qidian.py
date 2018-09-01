# -*- coding: utf-8 -*-
from copy import deepcopy

import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/all']

    def parse(self, response):
        b_list = response.xpath('//div[@class="all-book-list"]/div/ul/li')
        for i in b_list:
            item = {}
            item['imgurl'] = i.xpath('./div[@class="book-img-box"]/a/img/@src').extract_first()
            item['url'] = i.xpath('./div[@class="book-img-box"]/a/@href').extract_first()
            item['category'] = i.xpath('./div[@class="book-mid-info"]/p[@class="author"]/a[2]/text()').extract_first()
            item['author'] = i.xpath('./div[@class="book-mid-info"]/p[@class="author"]/a[1]/text()').extract_first()
            item['title'] = i.xpath('/div[@class="book-mid-info"]/h4/a/text()').extract_first()
            item['content'] = i.xpath('./div[@class="book-mid-info"]/p[@class="intro"]/text()').extract_first().strip()
            next_url = response.xpath('//li[@class="lbf-pagination-item"]/a[text()=">"]/@href').extract_first()
            next_url = 'http:'+next_url
            yield deepcopy(item)
            if next_url:
                yield scrapy.Request(next_url,callback=self.parse)

    # def detailparse(self,response):
    #     item = deepcopy(response.meta['item'])



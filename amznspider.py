import scrapy


class AmznspiderSpider(scrapy.Spider):
    name = 'amznspider'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class AmznspiderSpider(CrawlSpider):
    name = 'amznspider'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/s?k=laptops']

    rules = (
        Rule(LinkExtractor(allow='s?k=laptops&page=', restrict_css="a.s-pagination-next")),
        Rule(LinkExtractor(allow='/dp/'), callback='parse-item'),
    )

    def parse_item(self, response):
        pass

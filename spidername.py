import scrapy


class SpidernameSpider(scrapy.Spider):
    name = 'spidername'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s?rh=n%3A565108%2Cp_36%3A24218860']

    def parse(self, response):
        for link in response.css('h2.a-size-mini a::attr(href)'):
            yield response.follow(link, callback=self.parse_product)
        
    def parse_product(self, response):
        yield{
            'name': response.css('span#productTitle::text').get(),
            'price': response.css('span.a-offscreen::text').get(),
            'about': response.css('span.a-list-item::text').get()
        }

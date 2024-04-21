import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Special:Random']

    custom_settings = {
        'DEPTH_LIMIT': 3,
        'CLOSESPIDER_PAGECOUNT': 100,
        'AUTOTHROTTLE_ENABLED': True,
    }

    def parse(self, response):
        yield {
            'url': response.url,
            'content': response.text
        }
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)

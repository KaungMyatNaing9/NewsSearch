import scrapy

class WikiSpider(scrapy.Spider):
    name = 'wiki'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Contents/People_and_self',
                  'https://en.wikipedia.org/wiki/Wikipedia:Contents/Technology_and_applied_sciences',
                  'https://en.wikipedia.org/wiki/Wikipedia:Good_articles',
                  'https://en.wikipedia.org/wiki/Wikipedia:Contents/Natural_and_physical_sciences',
                  'https://en.wikipedia.org/wiki/Wikipedia:Contents/History_and_events']

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

import scrapy

class WikiSpider(scrapy.Spider):
    #A string that identifies the spider
    name = 'wiki'
    #A list of domains that the spider is allowed to crawl.
    allowed_domains = ['en.wikipedia.org']
    #A list of URLs where the spider will begin to crawl from.
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:Contents/People_and_self',
                  'https://en.wikipedia.org/wiki/Wikipedia:Contents/Technology_and_applied_sciences',
                  'https://en.wikipedia.org/wiki/Wikipedia:Good_articles',
                  'https://en.wikipedia.org/wiki/Wikipedia:Contents/Natural_and_physical_sciences',
                  'https://en.wikipedia.org/wiki/Wikipedia:Contents/History_and_events']

    #A dictionary of settings that will be used to configure the spider.
    custom_settings = {
        'DEPTH_LIMIT': 3,
        'CLOSESPIDER_PAGECOUNT': 300,
        'AUTOTHROTTLE_ENABLED': True,
    }

    #A method that will be called to handle the response downloaded for each of the requests made.
    def parse(self, response):
    # Extract the title of the article
        title = response.css('h1::text').get() or response.css('h1#firstHeading::text').get()

    # Extract the first paragraph or a summary
        summary = response.css('div.mw-parser-output > p:not([class])').xpath('normalize-space()').get()

    # Extract categories
        categories = response.css('div#mw-normal-catlinks ul li a::text').getall()

    # Extract infobox data (simple key-value pairs for demonstration)
        infobox = {
            box.css('th::text').get().strip(): box.css('td::text').get().strip()
            for box in response.css('table.infobox tr') if box.css('th::text') and box.css('td::text')
         }

    # Yield all extracted information
        yield {
            'url': response.url,
            'title': title,
            'summary': summary,
            'categories': categories,
            'infobox': infobox,
            'content': response.text  # including full content can be optional based on need
        }

    # Follow links to next pages
        for next_page in response.css('a::attr(href)'):
            yield response.follow(next_page, self.parse)


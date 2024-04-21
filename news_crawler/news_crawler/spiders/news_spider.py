import scrapy
from news_crawler.items import NewsItem

class CNNSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["cnn.com"]
    start_urls = [
        "https://www.cnn.com/world"
    ]

    def parse(self, response):
        # Extracting articles from the section
        for article in response.css('article.cd__content'):
            item = NewsItem()
            item['title'] = article.css('h3.cd__headline-text::text').get()
            item['author'] = article.css('.cd__byline span::text').get()
            item['publication_date'] = article.css('.update-time::attr(datetime)').get()
            item['content'] = self.parse_article(response.urljoin(article.css('a::attr(href)').get()))

            yield item

    def parse_article(self, article_url):
        # Parse individual article pages to extract content
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        return scrapy.Request(article_url, self.parse_article_content)

    def parse_article_content(self, response):
        # Extract full article text
        paragraphs = response.css('div.l-container p::text').getall()
        return ' '.join(paragraphs)

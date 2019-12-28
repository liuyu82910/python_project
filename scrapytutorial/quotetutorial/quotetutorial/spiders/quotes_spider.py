import scrapy
from quotetutorial.items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):

    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse (self, response):
        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')
        for q in all_div_quotes:
            title = q.css("span.text::text").extract()
            author = q.css("small.author::text").extract()
            tag = q.css("a.tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items




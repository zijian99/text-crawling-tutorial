import scrapy
from ..items import  QuotetutorialItem
class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self,response):
        # title to get the css, title::text to get the text without the <title> tag
        item = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:

            # Using class 
            item['title'] = quote.css('span.text::text').extract()
            item['author'] = quote.css('.author::text').extract()
            item['tag'] = quote.css('.tag::text').extract()

            yield item

            #Basic
            # title = quote.css('span.text::text').extract()
            # author = quote.css('.author::text').extract()
            # tag = quote.css('.tag::text').extract()
            # # yield{'titletext':quote}
            # yield{'titletext':title, 'author': author, 'tag':tag}
# BASE_URL = "https://books.toscrape.com/"
import scrapy

# try:
#     from _lzma import *
#     from _lzma import _encode_filter_properties, _decode_filter_properties
# except ImportError:
from backports.lzma import *
from backports.lzma import _encode_filter_properties, _decode_filter_properties


class BookSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for article in response.css("article.product_pod"):
            yield {
                "price": article.css(".price_color::text").extract_first(),
                "title": article.css("h3 > a::attr(title)").extract_first(),
            }

            next = response.css(".next > a::attr(href)").extract_first()
            if next:
                yield response.follow(next, self.parse)

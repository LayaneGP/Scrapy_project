import scrapy


class SneakerspiderSpider(scrapy.Spider):
    name = "sneakerspider"
    allowed_domains = ["nike.com.br"]
    start_urls = ["https://nike.com.br/snkrs/"]

    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    def parse(self, response):
        pass
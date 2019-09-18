import scrapy



class QuotesSpider(scrapy.Spider):
    name = "scname"

    def __init__(self, filename=None):
        if filename:
            with open(filename) as f:
                content = f.readlines()
                self.start_urls = ['https://twitter.com/'+x.strip() for x in content] #fuck this looping all listaaa
                    

    def parse(self, response):
        for title in response.css('title'):
            for quote in response.css('body.ms-windows'):
                yield {

                    'Title': title.css('title::text').extract_first(),
                    'Akun': quote.css('.ProfileWarningTimeline-heading::text').extract_first()
                    
                }
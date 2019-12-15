import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'alphabets'
    start_urls = [
        'https://www.drugs.com/alpha/condition/',
    ]

    def condition_parse(self, response):
        for alphabet in response.css('ul.ddc-list-column-2 li'):
            condition = alphabet.css('li a::text').extract_first()
            condition_url = alphabet.css('li a::attr("href")').get()
            
            if condition_url is not None:
                yield {
                    'condition': condition,
                    'condition_url': condition_url
                }
            

    def sub_alpha_parse(self, response):
        for alphabet in response.css('ul.ddc-paging li'):
            sub_alphabet = alphabet.css('li a::attr("href")').get()

            if sub_alphabet is not None:
                print(f'Working on {sub_alphabet}')
                yield response.follow(sub_alphabet, self.condition_parse)

    def parse(self, response):
        for alpha in response.css('ul.ddc-paging li'):
            alphabet = alpha.css('li a::attr("href")').get()

            if alphabet is not None:
                print(f'Working on {alphabet}')
                yield response.follow(alphabet, self.sub_alpha_parse)

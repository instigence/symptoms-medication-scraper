import pandas as pd
import scrapy
import requests

base_url = 'https://www.drugs.com'


class QuotesSpider(scrapy.Spider):
    name = 'alphabets'
    symptoms = pd.read_excel('conditions_with_urls.xlsx').to_dict(orient='records')
    all_urls = set([base_url + symptom['condition_url'] for symptom in symptoms])
    # Urls already fetched successfully
    previous_urls = set(pd.read_excel('conditions_urls_with_symptoms.xlsx')['condition_url'])

    start_urls = list(all_urls.difference(previous_urls))#[:10]
    print('Urls left to fetch %s' % len(start_urls))
    #print(start_urls)

    def parse(self, response):
        print('Fetching url %s' % response.url)
        try:
            #Recipe1
            # symptoms = response.css('.contentBox h2:contains("signs and symptoms")~ul')[0] \
            #     .get() \
            #     .replace("<ul>", "") \
            #     .replace("<li>", "") \
            #     .replace("</ul>", "") \
            #     .replace("</li>", "") \
            #     .split("\n")
            #Recipe2
            symptoms = response.css('.contentBox h2:contains("signs and symptoms")~p').get().replace("<p>","").replace("</p>", "").split("\n")
            if symptoms is not None:
                # symptoms["symptoms"] = list(filter(lambda sym: sym != '', symptoms))
                print(list(filter(lambda sym: sym != '', symptoms)))
                yield {
                    'condition': symptoms,
                    'condition_url': response.url
                }
        except Exception as e:
            print('Error Exist in parser, may be need to change parser rules.')


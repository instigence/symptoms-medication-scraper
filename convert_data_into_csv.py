import json
import pandas as pd


with open('data.json') as json_file:
    data = json.load(json_file)

pd.DataFrame(data).to_excel('conditions_with_urls.xlsx')
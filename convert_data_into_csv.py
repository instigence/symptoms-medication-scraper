import json
import pandas as pd

previous_data = pd.read_excel('conditions_urls_with_symptoms.xlsx')
new_data = pd.DataFrame()

with open('data.json') as json_file:
    data = json.load(json_file)
    new_data = pd.DataFrame(data)
updated_data = previous_data.append(new_data)
pd.DataFrame(updated_data).to_excel('conditions_urls_with_symptoms.xlsx', index=False)
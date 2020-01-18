import json

import pandas as pd

previous_data = pd.read_excel('conditions_urls_with_symptoms.xlsx')
new_data = pd.DataFrame()

with open('data.json') as json_file:
    data = json.load(json_file)
    new_data = pd.DataFrame(data)
updated_data = previous_data.append(new_data).to_dict(orient='records')

for symptom in updated_data:
    symptom['condition_url'] = symptom['condition_url'].replace('https://www.drugs.com', '')

pd.DataFrame(updated_data).to_excel('conditions_urls_with_symptoms.xlsx', index=False)

urls_success = [obj['condition_url'] for obj in updated_data]
all_urls = pd.read_excel('conditions_with_urls.xlsx').to_dict(orient='records')
for url in all_urls:
    if url['condition_url'] in urls_success:
        url['success'] = True

all_urls = pd.DataFrame(all_urls).to_excel('conditions_with_urls.xlsx', index=False)

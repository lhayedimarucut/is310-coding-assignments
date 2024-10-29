import os
import requests
import json


os.environ['EUROPEANA_API_KEY'] = "mmootrall"
europeana_api_key = os.getenv("EUROPEANA_API_KEY")


swapi_response = requests.get("https://swapi.dev/api/people/1/")  # Luke Skywalker
swapi_data = swapi_response.json()

europeana_url = (
    f"https://api.europeana.eu/record/v2/search.json?query={swapi_data['name']}"
    f"&wskey={europeana_api_key}&start=1&rows=5"
)

europeana_response = requests.get(europeana_url)
europeana_items = europeana_response.json().get('items', [])
europeana_data = []

#looking for the first title
for item in europeana_items:
    if 'title' in item:
        europeana_data.append(item['title'][0])  


combined_data = {
    'SWAPI': swapi_data,
    'Europeana': europeana_data
}

with open('swapi_europeana_data.json', 'w', encoding='utf-8') as f:
    json.dump(combined_data, f, ensure_ascii=False, indent=4)


    
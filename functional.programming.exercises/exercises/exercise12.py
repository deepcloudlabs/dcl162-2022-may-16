import json

# Find the minimum, the maximum and the average population of each continent.
with open('../resources/countries.json', encoding='utf-8') as json_file:
    countries = json.load(json_file)
    for country in countries:
        print(country['name'])

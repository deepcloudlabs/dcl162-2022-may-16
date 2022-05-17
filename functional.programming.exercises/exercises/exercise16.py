import json

# Find the cities with the minimum and the maximum population in countries.
with open('../resources/countries.json', encoding='utf-8') as json_file:
    countries = json.load(json_file)
    for country in countries:
        print(country['name'])

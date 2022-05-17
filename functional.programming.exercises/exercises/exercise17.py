import json

# Find the minimum, the maximum, the average, and the standard deviation of GNP values.
with open('../resources/countries.json', encoding='utf-8') as json_file:
    countries = json.load(json_file)
    for country in countries:
        print(country['name'])

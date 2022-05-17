import json

# Find the richest country of each continent with respect to their GNP (Gross National Product) values.
with open('../resources/countries.json', encoding='utf-8') as json_file:
    countries = json.load(json_file)
    for country in countries:
        print(country['name'])

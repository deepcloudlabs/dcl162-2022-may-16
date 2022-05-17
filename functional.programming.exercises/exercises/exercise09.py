import json

# Sort the countries by their population densities in descending order ignoring zero population countries
with open('../resources/countries.json', encoding='utf-8') as json_file:
    countries = json.load(json_file)
    for country in countries:
        print(country['name'])

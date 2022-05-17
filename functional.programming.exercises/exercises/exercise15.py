import json

# Group the countries by continent, and then sort the countries in continent by number of cities in each continent.
with open('../resources/countries.json', encoding='utf-8') as json_file:
    countries = json.load(json_file)
    for country in countries:
        print(country['name'])

import json

# Group the movies by the year and list them
with open('../resources/movies.json', encoding='utf-8') as json_file:
    movies = json.load(json_file)
    for movie in movies:
        print(movie['title'])

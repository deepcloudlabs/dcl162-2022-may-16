import json

# Find the year where the maximum number of movies is available
with open('../resources/movies.json', encoding='utf-8') as json_file:
    movies = json.load(json_file)
    for movie in movies:
        print(movie['title'])

import json

# Find the number of movies of each director
with open('../resources/movies.json', encoding='utf-8') as json_file:
    movies = json.load(json_file)
    for movie in movies:
        print(movie['title'])

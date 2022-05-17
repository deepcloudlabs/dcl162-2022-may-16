import json

# Find the number of genres of each director's movies
with open('../resources/movies.json', encoding='utf-8') as json_file:
    movies = json.load(json_file)
    for movie in movies:
        print(movie['title'])

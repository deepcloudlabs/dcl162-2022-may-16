import json

# Find the list of movies having the genres "Drama" and "Comedy" only
with open('../resources/movies.json', encoding='utf-8') as json_file:
    movies = json.load(json_file)
    for movie in movies:
        print(movie['title'])

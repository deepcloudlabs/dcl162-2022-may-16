"""
movies.json
Drama: 178
Comedy: 112
.
.
.
"""
import json

with open("resources/movies.json", mode="rt") as f:
    movies = json.load(f)
    histogram = {}
    for movie in movies:
        for genre in movie['genres']:
            genre_name = genre['name'].lower()
            if genre_name not in histogram:
                histogram[genre_name] = 1
            else:
                histogram[genre_name] += 1
    for genre_name, value in histogram.items():
        print(f"{genre_name}\t: {value}")

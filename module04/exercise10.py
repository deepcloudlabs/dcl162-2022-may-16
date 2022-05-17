import json
from functools import reduce


def to_histogram(histogram, genre_name):
    if genre_name not in histogram:
        histogram[genre_name] = 1
    else:
        histogram[genre_name] += 1
    return histogram


to_lower_genre_name = lambda genre: genre['name'].lower()
to_genres = lambda movie: movie['genres']

with open("resources/movies.json", mode="rt") as f:
    histogram = reduce(to_histogram, map(to_lower_genre_name, reduce(list.__add__, map(to_genres, json.load(f)))), {})
    for genre_name, count in sorted(histogram.items(), key=lambda item: item[1], reverse=True):
        print(f"{genre_name}\t: {count}")
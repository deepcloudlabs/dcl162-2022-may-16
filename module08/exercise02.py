from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

world_db = client['world']

for collection_name in world_db.list_collection_names():
    print(collection_name)
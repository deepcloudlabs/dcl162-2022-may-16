from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

for db_name in client.list_database_names():
    print(db_name)
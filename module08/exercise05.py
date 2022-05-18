from pymongo import MongoClient

from hr.domain import Employee

client = MongoClient("mongodb://localhost:27017")

hr_db = client['hr']  # hr database

employees = hr_db.employees  # employees collection

result = employees.delete_many({"birth_year": {"$gte": 1960, "$lt": 1970}})

print(f"{result.deleted_count} document(s) deleted.")

from pymongo import MongoClient

from hr.domain import Employee

client = MongoClient("mongodb://localhost:27017")

hr_db = client['hr']  # hr database

employees = hr_db.employees  # employees collection

result = employees.update_many(
    {"salary" : { "$gte": 50000}},
    {"$set": {"salary": 100000}}
)

print(f"{result.matched_count} document(s) selected")
print(f"Success: {result.acknowledged}")
print(f"{result.raw_result}")
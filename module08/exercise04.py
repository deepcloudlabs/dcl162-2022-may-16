from pymongo import MongoClient
from pprint import pprint as pp

from hr.domain import Employee

client = MongoClient("mongodb://localhost:27017")

hr_db = client['hr']  # hr database

employees = hr_db.employees  # employees collection
"""
    http://binkurt.blogspot.com/2015/02/mongodb-ile-calsmak.html
"""
for emp in employees.find({"$and": [{"birth_year": {"$gte": 1960, "$lt": 2000}}, {"salary": {"$gte": 75000}}]}).sort(
        "fullname", 1):
    pp(emp)

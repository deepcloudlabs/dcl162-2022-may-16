from pymongo import MongoClient

from hr.domain import Employee

client = MongoClient("mongodb://localhost:27017")

hr_db = client['hr']  # hr database

employees = hr_db.employees  # employees collection

emps = [
    Employee("1", "Jack Bauer", 100000, "jack@example.com", 1956, "tr1"),
    Employee("2", "Kate Austen", 200000, "kate@example.com", 1986, "tr2"),
    Employee("3", "Ben Linus", 100000, "linus@example.com", 1962, "tr3")
]
emps2 = [
    {"identity": "1", "fullname": "Jack Bauer", "salary": 100000, "email": "jack@example.com", "birth_year": 1956}
]
emps_dict = []
for emp in emps:
    emps_dict.append(emp.__dict__)

result = employees.insert_many(list(map(lambda emp: emp.__dict__, emps)))
print(f"inserted _id's: {result.inserted_ids}")

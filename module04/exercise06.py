import json

with open("employees.json", mode="rt") as f:
    employees = json.load(f)
    print(employees)

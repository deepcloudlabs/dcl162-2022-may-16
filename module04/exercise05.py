import json

employees = [
    {"iban": "tr1", "fullname": "jack shephard", "salary": 10_000},
    {"iban": "tr2", "fullname": "james sawyer", "salary": 20_000},
    {"iban": "tr3", "fullname": "kate austen", "salary": 30_000},
    {"iban": "tr4", "fullname": "jin kwon", "salary": 40_000}
]

with open("employees.json", mode="wt") as f:
    json.dump(employees, f)

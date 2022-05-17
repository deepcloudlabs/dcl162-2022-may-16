import csv

employees = [
    {"iban": "tr1", "fullname": "jack shephard", "salary": 10_000},
    {"iban": "tr2", "fullname": "james sawyer", "salary": 20_000},
    {"iban": "tr3", "fullname": "kate austen", "salary": 30_000},
    {"iban": "tr4", "fullname": "jin kwon", "salary": 40_000}
]

with open("employees.csv", mode="wt", newline='') as f:
    writer = csv.writer(f)
    for employee in employees:
        writer.writerow(employee.values())

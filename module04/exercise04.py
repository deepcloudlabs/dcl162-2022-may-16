import pickle

with open("employees.pkl", mode="rb") as f:
    employees = pickle.load(f)
    print(employees)

import pickle

employees = [
    ["tr1", "jack shephard", 10_000],
    ["tr2", "james sawyer", 20_000],
    ["tr3", "kate austen", 30_000],
    ["tr4", "jin kwon", 40_000]
]

with open("employees.pkl", mode="wb") as f:
    pickle.dump(employees, f)

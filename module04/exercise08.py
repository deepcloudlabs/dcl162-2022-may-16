import pandas as pd

df1 = pd.DataFrame([
    ["tr1", "jack shephard", 10_000],
    ["tr2", "james sawyer", 20_000],
    ["tr3", "kate austen", 30_000],
    ["tr4", "jin kwon", 40_000]
], columns=["iban", "full name", "salary"])

df1.to_csv("employees_df.csv")

df2 = pd.read_csv("employees_df.csv")
print(df2.index)
print(df2.columns)


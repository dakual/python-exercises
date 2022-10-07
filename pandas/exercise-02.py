import pandas as pd

df = pd.read_csv("sample2.csv")

pd.options.display.max_rows = 20
pd.set_option("display.min_rows", 5)

print(df)
print("---"*20)
print(df.head())
print("---"*20)
print(df.shape)
print("---"*20)
print(df.dtypes)
print("---"*20)
print(df.isnull().sum())
print("---"*20)
print(df.date.head())
print("---"*20)
print(df[["date","time"]].head())
print(df[["date","time"]].rename(columns={"date":"tarih","time":"zaman"}).head())
print("---"*20)
print(df.columns)
print("---"*20)
print(df.iloc[0].head())
print("---"*20)
print(df.iloc[0,[1,3,5]])
print("---"*20)
print(df.loc[1:5,"time":"type"])
print("---"*20)
print(df.loc[1:5,"time":"type"])
print("---"*20)
print(df.dropna(axis="columns",how="all").shape)
print("---"*20)
print(df.describe())
print("---"*20)
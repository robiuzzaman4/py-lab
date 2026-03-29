import pandas as pd

df = pd.read_csv("pokemon.csv")

# aggregate func for entire dataframe
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())

# single column
# print(df["Height"].mean()) # avg
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

# group by
group = df.groupby("Type1")
print(group["Height"].sum())

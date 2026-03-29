import pandas as pd

# import csv
df = pd.read_csv("pokemon.csv", index_col="Name")

# Selection by column
# print(df["Name"].to_string())
# print(df["Legendary"].to_string())
# # multi column
# print(df[["No", "Name", "Legendary"]].to_string())


# Selection by row
# print(df.loc[5])
# print(df.loc["Paras"])
print(df.loc["Paras", ["Height", "Weight"]])
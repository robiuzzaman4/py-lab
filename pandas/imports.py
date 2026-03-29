import pandas as pd

# import csv
df = pd.read_csv("pokemon.csv")
print(df.to_string())

# import json
df = pd.read_json("pokemon.json")
print(df.to_string())
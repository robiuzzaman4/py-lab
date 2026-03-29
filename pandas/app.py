import pandas as pd

df = pd.read_csv("pokemon.csv")

# 1. drop irrelevant columns
# df = df.drop(columns=["Legendary","No"])
df = df.drop(columns=["No"])

# 2. handle missing data (drop any pokemon if Type2 missing)
# df = df.dropna(subset=["Type2"])

# 2. handle missing data (replace any pokemon's Type2 with 'None' if Type2 missing)
df = df.fillna({"Type2": "None"})

# 3. Fix inconsistent values
df["Type1"] = df["Type1"].replace(
    {"Grass": "GRASS", "Fire": "FIRE", "Water": "WATER"}
)

# 4. Standardixe text
df["Name"]= df["Name"].str.lower()

# 5. Fix data type 
df["Legendary"] = df["Legendary"].astype(bool)

# 6. Remove duplicate values
df = df.drop_duplicates()

print(df.to_string())

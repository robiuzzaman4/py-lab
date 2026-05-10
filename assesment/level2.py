import pandas as pd

REGION = "Asia"

df = pd.read_csv("economy_data.csv")
df["Inflation_Rate"] = pd.to_numeric(df["Inflation_Rate"], errors="coerce")

asia = df[df["Region"] == REGION]
asia_inflation_data = asia.set_index("Country")["Inflation_Rate"].dropna().to_dict()

print(asia_inflation_data)

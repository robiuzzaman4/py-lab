import pandas as pd

COUNTRY = "Bangladesh"
FROM_YEAR = 1990
TO_YEAR = 2024

# read inflations and format
df = pd.read_csv("./data/inflation.csv", skiprows=4)
bd = df[df["Country Name"] == COUNTRY]

year_cols = [c for c in bd.columns if c.isdigit()]
df = bd.melt(
    id_vars=["Country Name", "Country Code",
             "Indicator Name", "Indicator Code"],
    value_vars=year_cols,
    var_name="Year",
    value_name="Inflation"
)

df["Year"] = df["Year"].astype(int)
df = df.sort_values("Year")

subset = df[(df["Year"] >= FROM_YEAR) & (df["Year"] <= TO_YEAR)]
print(subset[["Year", "Inflation"]].to_string())

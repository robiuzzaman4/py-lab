import pandas as pd

df = pd.read_csv('bangladesh_data.csv')
df = df.replace('..', pd.NA)
print(df)

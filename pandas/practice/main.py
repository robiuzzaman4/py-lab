import pandas as pd
import matplotlib.pyplot as plt

# load dataset & conver '..' into NaN
df = pd.read_csv('bangladesh_data.csv')
df = df.replace('..', pd.NA)

# clenup column name and text
df['Series Name'] = df['Series Name'].str.strip().str.replace('"', '')

# get agriculture & industrial data
agri_data = df[df['Series Name'].str.contains('Agriculture, forestry, and fishing, value added', case=False, na=False)]
ind_data = df[df['Series Name'].str.contains('Industry \(including construction\), value added', case=False, na=False)]

print(agri_data)
print(ind_data)
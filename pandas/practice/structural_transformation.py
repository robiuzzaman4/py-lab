import pandas as pd
import matplotlib.pyplot as plt

# load dataset & conver '..' into NaN
df = pd.read_csv('bangladesh_data.csv')
df = df.replace('..', pd.NA)

# clenup column name and text
df['Series Name'] = df['Series Name'].str.strip().str.replace('"', '')

# get agriculture & industrial data
agri_data = df[df['Series Name'].str.contains(
    'Agriculture, forestry, and fishing, value added', case=False, na=False)]
ind_data = df[df['Series Name'].str.contains(
    'Industry \(including construction\), value added', case=False, na=False)]

years = [
    '1990 [YR1990]', '2000 [YR2000]', '2016 [YR2016]', '2017 [YR2017]',
    '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]',
    '2022 [YR2022]', '2023 [YR2023]', '2024 [YR2024]', '2025 [YR2025]'
]

clean_years = [y.split(' ')[0] for y in years]

# convert data into number
agri_values = agri_data[years].values.flatten().astype(float)
ind_values = ind_data[years].values.flatten().astype(float)

# create graph
plt.figure(figsize=(11, 6))

# agri
plt.plot(clean_years, agri_values, marker='o', color='orange', linewidth=2.5, label='Agriculture (% of GDP)')

# ind
plt.plot(clean_years, ind_values, marker='s', color='blue', linewidth=2.5, label='Industry (% of GDP)')

# styling graph
plt.title('Structural Transformation in Bangladesh (1990 - 2025)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('% of GDP', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# add legend
plt.legend(fontsize=11)
plt.tight_layout()

# save and show
plt.savefig('structural_transformation.png')
print("✅ 'structural_transformation.png' নামে নতুন গ্রাফটি সেভ হয়েছে!")
plt.show()
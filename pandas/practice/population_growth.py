import pandas as pd
import matplotlib.pyplot as plt

# load dataset & conver '..' into NaN
df = pd.read_csv('bangladesh_data.csv')
df = df.replace('..', pd.NA)

# population growth
population_growth = df[df['Series Name'] == 'Population growth (annual %)']

years = [
    '1990 [YR1990]', '2000 [YR2000]', '2016 [YR2016]', '2017 [YR2017]',
    '2018 [YR2018]', '2019 [YR2019]', '2020 [YR2020]', '2021 [YR2021]',
    '2022 [YR2022]', '2023 [YR2023]', '2024 [YR2024]', '2025 [YR2025]'
]
# # convert year into pure number
values = population_growth[years].values.flatten().astype(float)
clean_years = [y.split(' ')[0] for y in years]

plt.figure(figsize=(10, 5))
plt.plot(clean_years, values, marker='o', color='green', linewidth=1)
plt.title('Bangladesh Annual Population Growth Rate (%)')
plt.xlabel('Year')
plt.ylabel('Growth Rate (%)')
plt.grid(True)
plt.savefig('population_growth.png')
print('saved population_growth.png ✅')
plt.show()

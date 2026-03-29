import pandas as pd

# === series ===
print("=== series ===")
data = [100, 200, 300]
data_series = pd.Series(data, index=["a", "b", "c"])
print(data_series)
print(data_series.loc["b"])
print(data_series.iloc[1])
print(data_series[data_series == 200])

calories = {"day-1": 1750, "day-2": 2100, "day-3": 2400}
calories_series = pd.Series(calories)
calories_series.loc["day-3"] += 500
print(calories_series.loc["day-3"])
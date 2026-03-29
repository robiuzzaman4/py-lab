import pandas as pd

# === data frames ===
print("=== data frames ===")

data = {
    "Name": ["Hia", "Han", "Ru"],
    "Age": [30, 25, 32]
}

df = pd.DataFrame(data)

# Add a new col
df["Job"] = ["Designer", "Developer", "Researcher"]

# Add a new row
new_rows = pd.DataFrame(
    [
        {
            "Name": "Ruhan",
            "Age": 24,
            "Job": "Engineer"
        },
        {
            "Name": "Taahia",
            "Age": 24,
            "Job": "Engineer"
        }
    ]
)
df = pd.concat([df, new_rows], ignore_index=True)

print(df)

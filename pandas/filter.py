import pandas as pd

df = pd.read_csv("pokemon.csv")

tall_pokemons = df[df["Height"] >= 2]
print("tall_pokemons", tall_pokemons)

heavy_pokemons = df[df["Weight"] >= 400]
print("heavy_pokemons", heavy_pokemons)

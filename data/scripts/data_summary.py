import pandas as pd

df = pd.read_csv("data/corn_yield_data.csv")

print(df.head())

print("\nSummary Statistics")

print(df.describe())

print("\nAverage Yield")

print(df["Yield_t_ha"].mean())

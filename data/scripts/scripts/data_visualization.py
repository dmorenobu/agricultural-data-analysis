import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/corn_yield_data.csv")

plt.scatter(df["Nitrogen_kg_ha"],df["Yield_t_ha"])

plt.xlabel("Nitrogen")

plt.ylabel("Yield")

plt.title("Nitrogen vs Yield")

plt.show()

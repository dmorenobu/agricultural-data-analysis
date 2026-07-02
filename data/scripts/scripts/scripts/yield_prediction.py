import pandas as pd

from sklearn.linear_model import LinearRegression

df=pd.read_csv("data/corn_yield_data.csv")

X=df[["Nitrogen_kg_ha","Rainfall_mm","Temperature_C"]]

y=df["Yield_t_ha"]

model=LinearRegression()

model.fit(X,y)

print(model.coef_)

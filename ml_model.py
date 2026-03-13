import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def train(df):

    if len(df)<15:
        return None

    X=df[[
    "sleep",
    "surf",
    "cannabis",
    "fishing",
    "food"
    ]]

    y=df["energy"]

    model=RandomForestRegressor()

    model.fit(X,y)

    return model

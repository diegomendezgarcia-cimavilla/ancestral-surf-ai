import pandas as pd

def dataframe(rows):

    columns=[
    "date",
    "energy",
    "mood",
    "stress",
    "sleep",
    "surf",
    "cannabis",
    "fishing",
    "food",
    "notes"
    ]

    return pd.DataFrame(rows,columns=columns)

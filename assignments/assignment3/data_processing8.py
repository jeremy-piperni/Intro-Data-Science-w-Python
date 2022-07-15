import pandas as pd
import numpy as np
import data_processing1

def answer_eight():
    df = data_processing1.answer_one()
    df["Population"] = (df["Energy Supply"] / df["Energy Supply per Capita"])
    df.sort_values(by="Population", ascending=False, inplace=True)
    df = df["Population"]
    country = df.index[2]
    return country

answer_eight()
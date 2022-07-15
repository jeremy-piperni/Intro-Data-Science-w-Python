import pandas as pd
import numpy as np
import data_processing1

def answer_six():
    df = data_processing1.answer_one()
    df.sort_values(by="% Renewable",ascending=False,inplace=True)
    df = df["% Renewable"]
    tuple = (df.index[0], df[0])
    return tuple

answer_six()
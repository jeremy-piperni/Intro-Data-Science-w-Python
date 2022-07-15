import pandas as pd
import numpy as np
import data_processing1

def answer_seven():
    df = data_processing1.answer_one()
    df["Citation Ratio"] = (df["Self-citations"] / df["Citations"])
    df.sort_values(by="Citation Ratio", ascending=False, inplace=True)
    df = df["Citation Ratio"]
    my_tuple = (df.index[0], df[0])
    return my_tuple

answer_seven()
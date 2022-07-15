import pandas as pd
import numpy as np
import data_processing1
import data_processing3

def answer_four():
    df = data_processing1.answer_one()
    series = data_processing3.answer_three()

    country = series.index[5]
    difference = df.loc[country]["2015"] - df.loc[country]["2006"]
    return difference

answer_four()

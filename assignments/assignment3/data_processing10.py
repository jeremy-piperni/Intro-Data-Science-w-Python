import pandas as pd
import numpy as np
import data_processing1

def answer_ten():
    df = data_processing1.answer_one()
    median = df["% Renewable"].median()
    df["High Renew"] = df["% Renewable"].apply(lambda x: check_renew(x, median))
    HighRenew = df["High Renew"]
    print(HighRenew)
    return HighRenew

def check_renew(x, median):
    if (x >= median):
        return 1
    if (x < median):
        return 0


answer_ten()
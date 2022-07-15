import pandas as pd
import numpy as np
import data_processing1

def answer_five():
    df = data_processing1.answer_one()
    num = df["Energy Supply per Capita"].mean()
    return num

answer_five()
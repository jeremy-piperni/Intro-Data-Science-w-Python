import pandas as pd
import numpy as np
import data_processing1

def answer_thirteen():
    df = data_processing1.answer_one()
    df["Population"] = (df["Energy Supply"] / df["Energy Supply per Capita"])
    PopEst = df["Population"].map("{:,}".format)
    
    return PopEst

answer_thirteen()
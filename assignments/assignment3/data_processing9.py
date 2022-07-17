import pandas as pd
import numpy as np
import scipy.stats as stats
import data_processing1

def answer_nine():
    df = data_processing1.answer_one()
    df["Population"] = (df["Energy Supply"] / df["Energy Supply per Capita"])
    df["Citable documents per Capita"] = df["Citable documents"] / df["Population"]

    corr, pval = stats.pearsonr(df["Citable documents per Capita"],df["Energy Supply per Capita"])
    return corr

answer_nine()
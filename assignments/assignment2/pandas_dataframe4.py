import scipy.stats as stats
import numpy as np
import pandas as pd

def corr_chickenpox():
    
    df = pd.read_csv('D://Data Science/Introduction to Data Science/assignments/assignment2/assets/NISPUF17.csv')
    #df = pd.read_csv('assets/NISPUF17.csv')

    df = df[(df['HAD_CPOX'] == 1) | (df['HAD_CPOX'] == 2)]
    df = df.dropna(subset=['HAD_CPOX','P_NUMVRC'])

    corr, pval = stats.pearsonr(df['HAD_CPOX'],df["P_NUMVRC"])
    return corr

print(corr_chickenpox())
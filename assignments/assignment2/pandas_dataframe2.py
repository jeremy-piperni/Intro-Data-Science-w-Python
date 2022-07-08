import pandas as pd
import numpy as np

def average_influenze_doses():

    df = pd.read_csv('D://Data Science/Introduction to Data Science/assignments/assignment2/assets/NISPUF17.csv')
    #df = pd.read_csv('assets/NISPUF17.csv')

    breastfed_df = df[df['CBF_01'] == 1]
    breastfed_influenza = breastfed_df['P_NUMFLU']
    total = np.sum(breastfed_influenza)/len(breastfed_influenza)

    non_breastfed_df = df[df['CBF_01'] != 1]
    non_breastfed_influenza = non_breastfed_df['P_NUMFLU']
    total2 = np.sum(non_breastfed_influenza)/len(non_breastfed_influenza)

    return (total, total2)

print(average_influenze_doses())
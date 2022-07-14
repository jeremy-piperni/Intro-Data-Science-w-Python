import pandas as pd
import numpy as np

def chickenpox_by_sex():
    
    df = pd.read_csv('D://Data Science/Introduction to Data Science/assignments/assignment2/assets/NISPUF17.csv')
    #df = pd.read_csv('assets/NISPUF17.csv')

    df.fillna(0, inplace=True)

    vaccinated = df[df['P_NUMVRC'] >= 1]
    vax_pox = vaccinated[vaccinated['HAD_CPOX'] == 1]
    vax_nopox = vaccinated[vaccinated['HAD_CPOX'] == 2]

    vax_pox_male = vax_pox[vax_pox['SEX'] == 1]
    vax_pox_female = vax_pox[vax_pox['SEX'] == 2]  

    vax_nopox_male = vax_nopox[vax_nopox['SEX'] == 1]
    vax_nopox_female = vax_nopox[vax_nopox['SEX'] == 2]

    male_ratio = len(vax_pox_male) / len(vax_nopox_male)
    female_ratio = len(vax_pox_female) / len(vax_nopox_female)

    return {'male': male_ratio, "female": female_ratio}

print(chickenpox_by_sex())

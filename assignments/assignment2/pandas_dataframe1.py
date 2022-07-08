import pandas as pd
import numpy as np

def proportion_of_education():

    df = pd.read_csv('D://Data Science/Introduction to Data Science/assignments/assignment2/assets/NISPUF17.csv')
    #df = pd.read_csv('assets/NISPUF17.csv')

    less_than_twelve = len(df[df['EDUC1'] == 1])
    twelve = len(df[df['EDUC1'] == 2])
    more_than_twelve = len(df[df['EDUC1'] == 3])
    college = len(df[df['EDUC1'] == 4])
    total = len(df['EDUC1'])

    less_than_twelve = less_than_twelve / total
    twelve = twelve / total
    more_than_twelve = more_than_twelve / total
    college = college / total

    dictionary = {"less than high school" : less_than_twelve,
                    "high school" : twelve,
                    "more than high school but not college" : more_than_twelve,
                    "college" : college}

    return dictionary

print(proportion_of_education())

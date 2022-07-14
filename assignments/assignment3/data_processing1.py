import pandas as pd
import numpy as np

def answer_one():

    Energy = pd.read_excel('D://Data Science/Introduction to Data Science/assignments/assignment3/assets/Energy Indicators.xls')
    #Energy = pd.read_excel('assets/Energy Indicators.xls')

    Energy.drop(index=Energy.index[0:17], axis=0, inplace=True)
    Energy.drop(columns=Energy.columns[0:2], axis=1, inplace=True)
    Energy.drop(index=Energy.tail(38).index, axis=0, inplace=True)
    Energy = Energy.rename(columns={"Unnamed: 2" : "Country", "Unnamed: 3" : "Energy Supply", "Unnamed: 4" : "Energy Supply per Capita", "Unnamed: 5" : "Renewable"})
    Energy["Energy Supply"] = 1000000 * Energy["Energy Supply"]
    Energy["Country"] = Energy["Country"].replace("[\d]*", "", regex=True)
    Energy["Country"] = Energy["Country"].replace(" \(.*?\)", "", regex=True)
    Energy["Country"] = Energy["Country"].replace({"Republic of Korea" : "South Korea", "United States of America" : "United States",
                                "United Kingdom of Great Britain and Northern Ireland" : "United Kingdom", "China, Hong Kong Special Administrative Region" : "Hong Kong"})
    
    GDP = pd.read_csv('D://Data Science/Introduction to Data Science/assignments/assignment3/assets/world_bank.csv')
    #GDP = pd.read_csv('assets/world_bank.csv')

    GDP.drop(index=GDP.index[0:3], axis=0, inplace=True)
    GDP.set_axis(GDP.loc[3], axis="columns", inplace=True)
    GDP.drop(index=GDP.index[0], axis=0, inplace=True)
    GDP["Country Name"] = GDP["Country Name"].replace({"Korea, Rep." : "South Korea", "Iran, Islamic Rep." : "Iran", "Hong Kong SAR, China" : "Hong Kong"})
    print(GDP.iloc[93])


answer_one()
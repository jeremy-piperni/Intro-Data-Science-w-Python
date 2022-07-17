import pandas as pd
import numpy as np
import data_processing1

def answer_twelve():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    df = data_processing1.answer_one()
    df["% Renewable"] = pd.cut(df["% Renewable"], 5)
    df["Continent"] = df.index.map(ContinentDict)
    df.reset_index(inplace=True)
    print(df)
    df = df[["Country", "Continent", "% Renewable"]]
    df.set_index(["Continent","% Renewable"], inplace=True)
    grouped = df.groupby(level=[0,1]).size()
    grouped = grouped.where(grouped > 0).dropna()

    return grouped

answer_twelve()
from hashlib import new
import pandas as pd
import numpy as np
import data_processing1

def answer_eleven():
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
    df["Continent"] = df.index.map(ContinentDict)
    df["Population"] = (df["Energy Supply"] / df["Energy Supply per Capita"])
    
    newdf = df.set_index("Continent").groupby(level = 0)["Population"].agg(size = np.size, sum = np.sum, mean = np.mean, std = np.std)
    return newdf

answer_eleven()
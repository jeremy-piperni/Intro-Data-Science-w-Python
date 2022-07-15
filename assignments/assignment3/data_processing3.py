import pandas as pd
import numpy as np
import data_processing1

def answer_three():
    df = data_processing1.answer_one()
    avgGDP = df[["2006","2007","2008","2009","2010","2011","2012","2013","2014","2015"]].mean(axis=1)
    avgGDP.sort_values(inplace=True,ascending=False)
    return avgGDP

answer_three()



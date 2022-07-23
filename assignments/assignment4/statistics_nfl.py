import pandas as pd
import numpy as np
import scipy.stats as stats
import re

def nfl_correlation():

    nfl_df=pd.read_csv("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/nfl.csv")
    #nfl_df=pd.read_csv("assets/nfl.csv")
    cities=pd.read_html("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/wikipedia_data.html")[1]
    #cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]
    
    nfl_df = nfl_df[nfl_df["year"]==2018]
    nfl_df["team"] = nfl_df["team"].str.strip()
    nfl_df.drop(index=[0,5,10,15,20,25,30,35], axis=0, inplace=True)
    nfl_df["team"] = nfl_df["team"].replace({"New York Giants" : "New York City Giants", "New York Jets" : "New York City Jets", "San Francisco 49ers" : "San Francisco Bay Area 49ers",
                                            "Oakland Raiders" : "San Francisco Bay Area Raiders"})
    nfl_df["team"].replace("\ \\w+$|\ \\w+\*$|\ \\w+\+$", "", regex=True, inplace=True)
    nfl_df["team"] = nfl_df["team"].replace({"Dallas" : "Dallas-Fort Worth", "Washington" : "Washington, D.C.", "New England" : "Boston", "Minnesota" : "Minneapolis-Saint Paul",
                                            "Miami" : "Miami-Fort Lauderdale", "Arizona" : "Phoenix", "Tampa Bay" : "Tampa Bay Area", "Carolina" : "Charlotte",
                                            "Tennessee" : "Nashville"})
    nfl_df = nfl_df.rename(columns={"team" : "City"})
    nfl_df.set_index("City", inplace=True)
    nfl_df["W-L%"] = pd.to_numeric(nfl_df["W-L%"])
    nfl_df = nfl_df.groupby("City").agg({"W-L%" : ["mean"]})


    cities = cities[~cities["NFL"].str.contains("—")]
    cities = cities[~cities["NFL"].str.contains("^\[.*\]", regex=True)]
    cities = cities.rename(columns={"Metropolitan area" : "City"})
    cities.set_index("City", inplace=True)
    cities["Population (2016 est.)[8]"] = pd.to_numeric(cities["Population (2016 est.)[8]"])
    cities = cities.groupby("City").agg({"Population (2016 est.)[8]" : ["sum"]})


    population_by_region = cities["Population (2016 est.)[8]"].to_numpy().flatten(order="C") # pass in metropolitan area population from cities
    win_loss_by_region = nfl_df["W-L%"].to_numpy().flatten(order="C") # pass in win/loss ratio from mlb_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q4: Your lists must be the same length"
    assert len(population_by_region) == 29, "Q4: There should be 29 teams being analysed for NFL"

    corr, pval = stats.pearsonr(population_by_region, win_loss_by_region)
    return corr

print(nfl_correlation())
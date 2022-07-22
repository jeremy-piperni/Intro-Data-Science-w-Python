import pandas as pd
import numpy as np
import scipy.stats as stats
import re

nhl_df=pd.read_csv("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/nhl.csv")
#nhl_df=pd.read_csv("assets/nhl.csv")

cities=pd.read_html("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/wikipedia_data.html")[1]
#cities=pd.read_html("assets/wikipedia_data.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]

def nhl_correlation(): 
    global nhl_df
    global cities
    nhl_df = nhl_df[nhl_df["year"]==2018]
    nhl_df.drop(index=[0,9,18,26], axis=0, inplace=True)
    nhl_df["team"] = nhl_df["team"].replace({"New York Islanders" : "New York City Islanders", "New York Rangers" : "New York City Rangers", "New Jersey Devils*" : "New York City Devils",
                                            "Anaheim Ducks*" : "Los Angeles Ducks"})
    nhl_df["team"].replace("\ \\w+$|\ \\w+\*$", "", regex=True, inplace=True)
    nhl_df["team"] = nhl_df["team"].replace({"Toronto Maple" : "Toronto", "Detroit Red" : "Detroit", "Columbus Blue" : "Columbus", "Vegas Golden" : "Las Vegas"})
    nhl_df["team"] = nhl_df["team"].replace({"San Jose" : "San Francisco Bay Area", "Dallas" : "Dallas-Fort Worth", "Washington" : "Washington, D.C.",
                                            "Minnesota" : "Minneapolis-Saint Paul", "Colorado" : "Denver", "Florida" : "Miami-Fort Lauderdale", "Arizona" : "Phoenix",
                                            "Tampa Bay" : "Tampa Bay Area", "Carolina" : "Raleigh"})
    nhl_df = nhl_df.rename(columns={"team" : "City"})
    nhl_df.set_index("City", inplace=True)
    nhl_df["W"] = pd.to_numeric(nhl_df["W"])
    nhl_df["L"] = pd.to_numeric(nhl_df["L"])
    nhl_df = nhl_df.groupby("City").agg({"W" : ["sum"], "L" : ["sum"]})
    nhl_df["Ratio"] = (nhl_df["W"] / (nhl_df["W"] + nhl_df["L"]))
    nhl_df.drop(["W","L"],axis=1,inplace=True)

    print(nhl_df)

    cities = cities[~cities["NHL"].str.contains("—")]
    cities = cities[~cities["NHL"].str.contains("^\[.*\]", regex=True)]
    cities = cities.rename(columns={"Metropolitan area" : "City"})
    cities.set_index("City", inplace=True)
    cities["Population (2016 est.)[8]"] = pd.to_numeric(cities["Population (2016 est.)[8]"])
    cities = cities.groupby("City").agg({"Population (2016 est.)[8]" : ["sum"]})

    print(cities)
    
    population_by_region = cities["Population (2016 est.)[8]"].to_numpy().flatten(order="C") # pass in metropolitan area population from cities
    win_loss_by_region = nhl_df["Ratio"].to_numpy() # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q1: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q1: There should be 28 teams being analysed for NHL"
    
    print(population_by_region)

    corr, pval = stats.pearsonr(population_by_region, win_loss_by_region)
    return corr

print(nhl_correlation())
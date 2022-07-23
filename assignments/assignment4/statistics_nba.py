import pandas as pd
import numpy as np
import scipy.stats as stats
import re

def nba_correlation():

    nba_df=pd.read_csv("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/nba.csv")
    #nba_df=pd.read_csv("assets/nba.csv")
    cities=pd.read_html("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/wikipedia_data.html")[1]
    #cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]
    
    nba_df = nba_df[nba_df["year"]==2018]
    nba_df["team"].replace("\(.*\)$", "", regex=True, inplace=True)
    nba_df["team"] = nba_df["team"].str.strip()
    nba_df["team"] = nba_df["team"].replace({"New York Knicks" : "New York City Knicks", "Brooklyn Nets" : "New York City Nets"})
    nba_df["team"].replace("\ \\w+$|\ \\w+\*$", "", regex=True, inplace=True)
    nba_df["team"] = nba_df["team"].replace({"Portland Trail" : "Portland", "Golden State" : "San Francisco Bay Area", "Dallas" : "Dallas-Fort Worth", "Washington" : "Washington, D.C.",
                                            "Minnesota" : "Minneapolis-Saint Paul", "Miami" : "Miami-Fort Lauderdale", "Indiana" : "Indianapolis", "Utah" : "Salt Lake City"})
    nba_df = nba_df.rename(columns={"team" : "City"})
    nba_df.set_index("City", inplace=True)
    nba_df["W/L%"] = pd.to_numeric(nba_df["W/L%"])
    nba_df = nba_df.groupby("City").agg({"W/L%" : ["mean"]})

    cities = cities[~cities["NBA"].str.contains("—")]
    cities = cities[~cities["NBA"].str.contains("^\[.*\]", regex=True)]
    cities = cities.rename(columns={"Metropolitan area" : "City"})
    cities.set_index("City", inplace=True)
    cities["Population (2016 est.)[8]"] = pd.to_numeric(cities["Population (2016 est.)[8]"])
    cities = cities.groupby("City").agg({"Population (2016 est.)[8]" : ["sum"]})

    population_by_region = cities["Population (2016 est.)[8]"].to_numpy().flatten(order="C") # pass in metropolitan area population from cities
    win_loss_by_region = nba_df["W/L%"].to_numpy().flatten(order="C") # pass in win/loss ratio from nhl_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q2: Your lists must be the same length"
    assert len(population_by_region) == 28, "Q2: There should be 28 teams being analysed for NBA"

    corr, pval = stats.pearsonr(population_by_region, win_loss_by_region)
    return corr

print(nba_correlation())
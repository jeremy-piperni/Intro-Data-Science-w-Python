import pandas as pd
import numpy as np
import scipy.stats as stats
import re

def mlb_correlation():

    mlb_df=pd.read_csv("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/mlb.csv")
    #mlb_df=pd.read_csv("assets/mlb.csv")
    cities=pd.read_html("D://Data Science/Introduction to Data Science/assignments/assignment4/assets/wikipedia_data.html")[1]
    #cities=pd.read_html("assets/wikipedia_data.html")[1]
    cities=cities.iloc[:-1,[0,3,5,6,7,8]]
    
    mlb_df = mlb_df[mlb_df["year"]==2018]
    mlb_df["team"] = mlb_df["team"].str.strip()
    mlb_df["team"] = mlb_df["team"].replace({"New York Yankees" : "New York City Yankees", "New York Mets" : "New York City Mets", "San Francisco Giants" : "San Francisco Bay Area Giants",
                                            "Oakland Athletics" : "San Francisco Bay Area Athletics"})
    mlb_df["team"].replace("\ \\w+$", "", regex=True, inplace=True)
    mlb_df["team"] = mlb_df["team"].replace({"Boston Red" : "Boston", "Toronto Blue" : "Toronto", "Chicago White" : "Chicago", "Texas" : "Dallas-Fort Worth", "Washington" : "Washington, D.C.",
                                            "Minnesota" : "Minneapolis-Saint Paul", "Colorado" : "Denver", "Miami" : "Miami-Fort Lauderdale", "Arizona" : "Phoenix",
                                            "Tampa Bay" : "Tampa Bay Area"})
    mlb_df = mlb_df.rename(columns={"team" : "City"})
    mlb_df.set_index("City", inplace=True)
    mlb_df["W-L%"] = pd.to_numeric(mlb_df["W-L%"])
    mlb_df = mlb_df.groupby("City").agg({"W-L%" : ["mean"]})

    cities = cities[~cities["MLB"].str.contains("—")]
    cities = cities[~cities["MLB"].str.contains("^\[.*\]", regex=True)]
    cities = cities.rename(columns={"Metropolitan area" : "City"})
    cities.set_index("City", inplace=True)
    cities["Population (2016 est.)[8]"] = pd.to_numeric(cities["Population (2016 est.)[8]"])
    cities = cities.groupby("City").agg({"Population (2016 est.)[8]" : ["sum"]})

    population_by_region = cities["Population (2016 est.)[8]"].to_numpy().flatten(order="C") # pass in metropolitan area population from cities
    win_loss_by_region = mlb_df["W-L%"].to_numpy().flatten(order="C") # pass in win/loss ratio from mlb_df in the same order as cities["Metropolitan area"]
    assert len(population_by_region) == len(win_loss_by_region), "Q3: Your lists must be the same length"
    assert len(population_by_region) == 26, "Q3: There should be 26 teams being analysed for MLB"

    corr, pval = stats.pearsonr(population_by_region, win_loss_by_region)
    return corr

print(mlb_correlation())
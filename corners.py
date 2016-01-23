# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:55:56 2015

@author: Adetola
"""


from pandas import DataFrame
import pandas as pd
pd.set_option('precision',4)

# Read corner data
date = 'Date'
home_team = 'HomeTeam'
away_team = 'AwayTeam'
home_shoot = 'HS'
away_shoot = 'AS'
home_corner = 'HC'
away_corner = 'AC'
column = [date, home_team, away_team, home_corner, away_corner, home_shoot, away_shoot]
data = pd.read_csv('data/corners.csv')

# List of teams in dataset
team_list = DataFrame(sorted(data[home_team].unique()), columns=['Teams'])
team_A = 'Chelsea'
team_B = 'Arsenal'
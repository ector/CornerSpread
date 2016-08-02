# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:55:56 2015

@author: Adetola
"""

from __future__ import division
from pandas import DataFrame
import pandas as pd
import numpy as np
from simulate import corner_spread

pd.set_option('precision', 2)

# Read corner data
date = 'Date'
home_team = 'HomeTeam'
away_team = 'AwayTeam'
home_shoot = 'HS'
away_shoot = 'AS'
home_corner = 'HC'
away_corner = 'AC'
corner_sum = 'CS'
column = [date, home_team, away_team, home_corner, away_corner, home_shoot, away_shoot]
data = pd.read_csv('data/corners.csv')

# List of teams in dataset
team_list = DataFrame(sorted(data[home_team].unique()), columns=['Teams'])
team_A = 'Liverpool'
team_B = 'Chelsea'

if team_A in team_list.values and team_B in team_list.values:
    data = data[(data['HomeTeam'] == team_A) & (data['AwayTeam'] == team_B)]

data.loc[:, 'CS'] = data[['HC', 'AC']].sum(1)
period = len(data.CS)
data.loc[:, 'C_CS'] = pd.rolling_mean(data.CS, period, 1)

datatest = data[:-1]
last_match = datatest.tail(1)
next_match = data.tail(1)

probmat = np.array([[0.0] * 9] * 9)
# matrix representation of home and away team runs for table
homemat = np.array([[9] * 9, [8] * 9, [7] * 9, [6] * 9, [5] * 9, [4] * 9, [3] * 9, [2] * 9, [1] * 9])
awayrow = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
awaymat = np.array([awayrow] * 9)
niterations = 1000

for index_home in range(9):
    for index_away in range(9):
        if homemat[index_home, index_away] != awaymat[index_home, index_away]:
            probmat[index_home, index_away] = corner_spread(float(homemat[index_home, index_away]),
                                                            float(awaymat[index_home, index_away]), last_match.C_CS,
                                                            niterations)

cornermat = DataFrame(probmat, index=range(9, 0, -1), columns=range(1, 10))

print(last_match)
print('=============================================================')
print(next_match)
print('============== ' + team_A + ' vs ' + team_B + ' ==============')
print(cornermat)

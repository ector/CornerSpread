# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 01:33:10 2016

@author: Adetola
"""
from __future__ import division
from scipy.stats import nbinom
import numpy.random as random


def corner_spread(home_corners, away_corners, corner_mean, niterations):
    random.seed(1234)
    game_home_mean = [0] * niterations
    game_away_mean = [0] * niterations
    game_corner_mean = [0] * niterations
    over_corner_mean_counter = [0] * niterations
    i = 0
    n_count = 4.0
    while i < niterations:
        game_home_mean[i] = nbinom.rvs(n=n_count, p=n_count / (n_count + home_corners), size=1)[0]
        game_away_mean[i] = nbinom.rvs(n=n_count, p=n_count / (n_count + away_corners), size=1)[0]
        game_corner_mean[i] = nbinom.rvs(n=n_count, p=n_count / (n_count + corner_mean), size=1)[0]
        home_plus_away = game_home_mean[i] + game_away_mean[i]
        if home_plus_away > game_corner_mean[i]:
            over_corner_mean_counter[i] = 1
        if (game_corner_mean[i] > home_plus_away) or (game_corner_mean[i] < home_plus_away):
            i += 1
    n_over_corner_mean_count = sum(over_corner_mean_counter)
    return n_over_corner_mean_count / float(niterations)

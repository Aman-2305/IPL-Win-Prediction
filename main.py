# -*- coding: utf-8 -*-
"""
Created on Tue May 27 12:50:15 2025

@author: Aman Srivastava
"""
import pandas as pd
import numpy as np

match = pd.read_csv('tempdata/matches.csv')
delivery = pd.read_csv('tempdata/deliveries.csv')

#MADE A GROUPBY FOR INNINGS AND SUMMED TOTAL_SCORE. CREATED ITS DF
total_score_df = delivery.groupby(['match_id', 'inning']).sum()['total_runs'].reset_index() 
#total_score_df

#FILTERED DATA TO CONSIST ONLY 1ST INNING.
total_score_df = total_score_df[total_score_df['inning'] == 1]
#total_score_df

match_df = match.merge(total_score_df[['match_id', 'total_runs']], left_on='id', right_on='match_id')
#match_df

teams = [
    'Chennai Super Kings',
	'Mumbai Indians',
    'Kolkata Knight Riders',
	'Sunrisers Hyderabad',
    'Rajasthan Royals',
	'Gujarat Titans',
    'Royal Challengers Bengaluru',
	'Delhi Capitals',
    'Punjab Kings',
	'Lucknow Super Giants',
]

match_df['team1'] = match_df['team1'].str.replace('Delhi Daredevils', 'Delhi Capitals')
match_df['team2'] = match_df['team2'].str.replace('Delhi Daredevils', 'Delhi Capitals')

match_df['team1'] = match_df['team1'].str.replace('Deccan Chargers', 'Sunrisers Hyderabad')
match_df['team2'] = match_df['team2'].str.replace('Deccan Chargers', 'Sunrisers Hyderabad')

match_df['team1'] = match_df['team1'].str.replace('Royal Challengers Bangalore', 'Royal Challengers Bengaluru')
match_df['team2'] = match_df['team2'].str.replace('Royal Challengers Bangalore', 'Royal Challengers Bengaluru')

match_df['team1'] = match_df['team1'].str.replace('Kings XI Punjab', 'Punjab Kings')
match_df['team2'] = match_df['team2'].str.replace('Kings XI Punjab', 'Punjab Kings')

match_df['team1'] = match_df['team1'].str.replace('Gujarat Lions', 'Gujarat Titans')
match_df['team2'] = match_df['team2'].str.replace('Gujarat Lions', 'Gujarat Titans')

match_df = match_df[match_df['team1'].isin(teams)]
match_df = match_df[match_df['team2'].isin(teams)]



match_df = match_df[['match_id','city','winner','total_runs']]
delivery_df = match_df.merge(delivery, on='match_id')

delivery_df = delivery_df[delivery_df['inning'] == 2]

delivery_df['current_score'] = delivery_df.groupby('match_id')['total_runs_y'].cumsum()
delivery_df['runs_left'] = delivery_df['total_runs_x'] - delivery_df['current_score']











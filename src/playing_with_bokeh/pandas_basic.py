"""
 Created on 25 Aug 2019
"""
import pandas as pd
from src.playing_with_bokeh import plots_output
from bokeh.io import output_file

playerBoxScore = plots_output.data_in("2017-18_playerBoxScore.csv")
teamBoxScore = plots_output.data_in("2017-18_teamBoxScore.csv")
standings = plots_output.data_in("2017-18_standings.csv")

player_stats = pd.read_csv(playerBoxScore, parse_dates=['gmDate'])
team_stats = pd.read_csv(teamBoxScore, parse_dates=['gmDate'])
standings = pd.read_csv(standings, parse_dates=['stDate'])

output_file(plots_output.plot_out('basic_pandas'),
            title="PAndas Plotting Example")
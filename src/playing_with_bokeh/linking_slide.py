"""
 Created on 25 Aug 2019
"""
import pandas as pd
from src.playing_with_bokeh import plots_output
# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, Div
from bokeh.layouts import gridplot, column

playerBoxScore = plots_output.data_in("2017-18_playerBoxScore.csv")
teamBoxScore = plots_output.data_in("2017-18_teamBoxScore.csv")
standings = plots_output.data_in("2017-18_standings.csv")

player_stats = pd.read_csv(playerBoxScore, parse_dates=['gmDate'])
team_stats = pd.read_csv(teamBoxScore, parse_dates=['gmDate'])
standings = pd.read_csv(standings, parse_dates=['stDate'])

phi_gm_stats = (team_stats[(team_stats["teamAbbr"] == "PHI") &
                           (team_stats["seasTyp"] == "Regular")]
                           .loc[:, ["gmDate",
                                    "teamPTS",
                                    "teamTRB",
                                    "teamAST",
                                    "teamTO",
                                    "opptPTS",]]
                           .sort_values("gmDate")
                           )

# Add game number
phi_gm_stats["game_num"] = range(1, len(phi_gm_stats)+1)

# Derive a win_loss columns
win_loss = []
for _, row in phi_gm_stats.iterrows():
    # if the 76ers score more it is a win
    if row["teamPTS"] > row["opptPTS"]:
        win_loss.append("W")
    else:
        win_loss.append("L")
phi_gm_stats["winLoss"] = win_loss

print(phi_gm_stats.head())

# PLOTTING

output_file(plots_output.plot_out('linking_slide'),
            title="Linking Slide Example")
gm_stats_cds = ColumnDataSource(phi_gm_stats)
# Crate categoricalColorMaper that signs a color to wins and losses
# a list specifying the categorical data values to be mapped is passed to factors and a list with the intended colors to palette.
win_loss_mapper = CategoricalColorMapper(factors = ["W", "L"],
                                         palette=["green", "red"])

# Creating four plots by looping 
stat_names = {"Points": "teamPTS",
              "Assists": "teamAST",
              "Rebounds": "teamTRB",
              "Turnovers": "teamTO"}
# dictionary for all four figures:
stat_figs = {}

# create y looping
for stat_label, stat_col in stat_names.items():
    # create individual figure
    fig = figure(y_axis_label=stat_label, 
                 plot_height=200, plot_width=400, 
                 x_range=(1, 10), tools=["xpan", "reset", "save"])
    # configure vbar
    fig.vbar(x="game_num", top=stat_col, source=gm_stats_cds, width=0.9,
             color=dict(field="winLoss", transform=win_loss_mapper))
    # Add the figure to stat_figs
    stat_figs[stat_label] =fig
    
# create layout
grid = gridplot([[stat_figs["Points"], stat_figs["Assists"]],
                 [stat_figs["Rebounds"], stat_figs["Turnovers"]]])

# SETTING EQUAL X RANGE:
stat_figs["Points"].x_range = \
    stat_figs["Assists"].x_range = \
    stat_figs["Rebounds"].x_range = \
    stat_figs["Turnovers"].x_range
    
# ADDING HTML RENDERING
html = """<h3>Philadelphia 76ers Game Log</h3>
<b><i>2017-18 Regular Seazon</i>
<br>
</b><i>Wins in green, losses in red</i>
"""
sup_title = Div(text=html)

show(column(sup_title, grid))
    
"""
 Created on 25 Aug 2019
"""
import pandas as pd
from src.playing_with_bokeh import plots_output
# Bokeh Libraries
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CategoricalColorMapper, NumeralTickFormatter
from bokeh.layouts import gridplot

teamBoxScore = plots_output.data_in("2017-18_teamBoxScore.csv")

team_stats = pd.read_csv(teamBoxScore, parse_dates=['gmDate'])

phi_gm_stats_2 = (team_stats[(team_stats["teamAbbr"] == "PHI") &
                           (team_stats["seasTyp"] == "Regular")]
                           .loc[:, ["gmDate",
                                    "team2P%",
                                    "team3P%",
                                    "teamPTS",
                                    "opptPTS",]]
                           .sort_values("gmDate")
                           )
# Add game number
phi_gm_stats_2['game_num'] = range(1, len(phi_gm_stats_2) + 1)

# Derive a win_loss column
win_loss = []
for _, row in phi_gm_stats_2.iterrows():

    # If the 76ers score more points, it's a win
    if row['teamPTS'] > row['opptPTS']:
        win_loss.append('W')
    else:
        win_loss.append('L')

# Add the win_loss data to the DataFrame
phi_gm_stats_2['winLoss'] = win_loss

print(phi_gm_stats_2.head())

output_file(plots_output.plot_out('linking_selection'),
            title="Linking Selection Example")

gm_stats_cds = ColumnDataSource(phi_gm_stats_2)
win_loss_mapper = CategoricalColorMapper(factors=["W", "L"], palette=["Green", "red"])

toolList = ['lasso_select', 'tap', 'reset', "save"]

pctFig = figure(title="2PT FG % vs 3PT FG %, 2017-18 regular",
                plot_height=400, plot_width=400, tools=toolList,
                x_axis_label="2PT FG%", y_axis_label="3PT FG%")
pctFig.circle(x="team2P%", y="team3P%", source=gm_stats_cds, size=12, color='black')

pctFig.xaxis[0].formatter = NumeralTickFormatter(format="00.0%")
pctFig.yaxis[0].formatter = NumeralTickFormatter(format="00.0%")

toFig = figure(title='Team Points vs Opponent Points, 2017-18 Regular Season',
                plot_height=400, plot_width=400, tools=toolList,
                x_axis_label='Team Points', y_axis_label='Opponent Points')
toFig.square(x='teamPTS', y='opptPTS', source=gm_stats_cds, size=10,
              color=dict(field='winLoss', transform=win_loss_mapper))

grid = gridplot([[pctFig, toFig]])

show(grid)


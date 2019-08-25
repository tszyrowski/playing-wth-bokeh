"""
 Created on 25 Aug 2019
"""
import pandas as pd
from src.playing_with_bokeh import plots_output
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, CDSView, GroupFilter
from bokeh.plotting import figure, show


playerBoxScore = plots_output.data_in("2017-18_playerBoxScore.csv")
teamBoxScore = plots_output.data_in("2017-18_teamBoxScore.csv")
standings = plots_output.data_in("2017-18_standings.csv")

player_stats = pd.read_csv(playerBoxScore, parse_dates=['gmDate'])
team_stats = pd.read_csv(teamBoxScore, parse_dates=['gmDate'])
standings = pd.read_csv(standings, parse_dates=['stDate'])


west_top_2 = (standings[(standings['teamAbbr'] == 'HOU') | (standings['teamAbbr'] == 'GS')]
                        .loc[:, ['stDate', 'teamAbbr', 'gameWon']]
                        .sort_values(['teamAbbr','stDate']))
print(west_top_2.head())

output_file(plots_output.plot_out('basic_pandas'),
            title="Pandas Plotting Example")

def create_step_1():
    """Create step plot by manipulating pandas to return two ColumnDataSource"""
    
    # Create to separate sets for teams
    rockets_data = west_top_2[west_top_2["teamAbbr"] == "HOU"]
    warriors_data = west_top_2[west_top_2["teamAbbr"] == "GS"]
    
    rockets_cds = ColumnDataSource(rockets_data)
    warriors_cds = ColumnDataSource(warriors_data)
    
    fig = figure(x_axis_type="datetime",
                 plot_height=300, plot_width=600, 
                 title="Wsetern Conf Top 2 Teams",
                 x_axis_label="Date", y_axis_label="Wins",
                 toolbar_location=None
                 )
    
    fig.step("stDate", "gameWon", color="#CE1141", legend="Rockets", source=rockets_cds)
    
    fig.step("stDate", "gameWon", color="#006BB6", legend="Warriors", source=warriors_cds)
    
    fig.legend.location="top_left"
    
    return fig

def create_step_2():
    """Create step by applying filter in ColumnDataSource"""
    
    west_cds = ColumnDataSource(west_top_2)
    
    rockets_view = CDSView(source=west_cds, 
                           filters=[GroupFilter(column_name="teamAbbr", group="HOU")])
    warriors_view = CDSView(source=west_cds, 
                           filters=[GroupFilter(column_name="teamAbbr", group="GS")])
    fig = figure(x_axis_type="datetime",
                  plot_height=300, plot_width=600,
                  title='Western Conference Top 2 Teams Wins Race, 2017-18',
                  x_axis_label='Date', y_axis_label='Wins',
                  toolbar_location=None)
                  
    fig.step('stDate', 'gameWon',
                  source=west_cds, view=rockets_view,
                  color='#CE1141', legend='Rockets')
    fig.step('stDate', 'gameWon',
                  source=west_cds, view=warriors_view,
                  color='#006BB6', legend='Warriors')
    return fig

if __name__=="__main__":
    fig = create_step_2()

    show(fig)
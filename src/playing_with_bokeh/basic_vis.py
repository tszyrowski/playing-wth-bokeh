"""
 Created on 24 Aug 2019
 
 based on:
 https://realpython.com/python-data-visualization-bokeh/
"""
import pandas as pd
import numpy as np

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from src.playing_with_bokeh import plots_output

# The data will be created as name.html
output_file(plots_output.plot_out('first_plot'), title="Empyt Bokeh Figure")
# render inline with jupiter notebook
# output_notebook() # will give an error if no Ipython installed


fig = figure() # inistantiate a figure objet

show(fig)
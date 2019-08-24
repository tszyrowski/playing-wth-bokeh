"""
 Created on 24 Aug 2019
"""
from src.playing_with_bokeh import plots_output
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models.annotations import ColorBar
from bokeh.models.mappers import LinearColorMapper
from bokeh.models.ranges import Range1d

output_file(plots_output.plot_out('basic_data'),
            title="Example of basic data plotting")

x = [1,2,4,7,5,3]
y = [x**2 for x in x]

x_range = Range1d(start = 0, end = max(x)+2, bounds = (0, max(x)+5))    # makes plot
y_range = Range1d(start = 0, end = max(y)+2, bounds = (0, max(y)+5))    # without white spaces


plot_width=100                                  # sets width of the plot to a given value
plot_height=int(plot_width * (max(y)/max(x)))   # gets proportional hight
fig = figure(title="Basic plot",
#              plot_height=300, plot_width=300,
#              sizing_mode='stretch_both', # this will get full screen 
#              aspect_ratio=0.5, # changes widt, but not exactly shure how
             plot_width = plot_width, plot_height = plot_height,
             x_range = x_range, y_range = y_range,
             match_aspect=True,                     # will get similar aspect in pixels, square is square
#              x_range=(0, max(x)+1), y_range=(0, max(y)+1),
             toolbar_location=None)

fig.circle(x=x, y=y, color="green", size=10, alpha=0.7)

show(fig)


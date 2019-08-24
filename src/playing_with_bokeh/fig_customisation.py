"""
 Created on 24 Aug 2019
 
 Show customisation of the figure canvas
 
 based on:
 https://realpython.com/python-data-visualization-bokeh/
"""
from bokeh.io import output_file
from bokeh.plotting import figure, show
from src.playing_with_bokeh import plots_output

output_file(plots_output.plot_out('customised_figure'),
            title="Example of Figure customisation")

fig = figure(background_fill_color="gray",
             background_fill_alpha=0.5,
             border_fill_color="blue",
             border_fill_alpha=0.25,
             plot_height=300,
             plot_width=500,
             h_symmetry=True,
             x_axis_label="X Label",
             x_axis_type="datetime",
             x_axis_location="above",
             x_range=("2019-01-01", "2019-08-30"),
             y_axis_label="Y Label",
             y_axis_type="linear",
             y_axis_location="left",
             y_range=(0, 100),
             title="Example Figure",
             title_location="right",
             toolbar_location="below",
             tools="save"
             )

# modifying after instantioation
fig.grid.grid_line_color = "red"
show(fig)
"""
 Created on 25 Aug 2019
"""
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models.tools import PanTool, SaveTool
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource, BoxZoomTool, WheelZoomTool, LassoSelectTool, BoxSelectTool, ResetTool, \
    PanTool, TapTool, SaveTool
from src.playing_with_bokeh import plots_output

output_file(plots_output.plot_out('remove_logo'), title="No Logo")

tools = [PanTool(), BoxZoomTool(match_aspect=True), WheelZoomTool(), BoxSelectTool(),
         ResetTool(), TapTool(), SaveTool()]

figures = [figure(plot_width=800, plot_height=800,
                  tools=tools, output_backend="webgl", match_aspect=True) for i in range(2)]

figures[0].line([1, 2, 3, 4], [1, 4, 3, 0])
figures[0].toolbar.logo = None              # this line removes logo

figures[1].line([1, 2, 3, 4], [1, 4, 3, 0])
figures[1].toolbar.logo = None

grid = gridplot([figures], 
                merge_tools=True, 
                sizing_mode='scale_height',
                toolbar_options=dict(logo=None))    # removes logo from grid
show(grid)
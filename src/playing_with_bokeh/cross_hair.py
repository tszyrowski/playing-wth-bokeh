from bokeh.io import show, output_file, save, show
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models.sources import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models.callbacks import CustomJS
from src.playing_with_bokeh import plots_output

output_file(plots_output.plot_out("cross_hair.html"), title="Empyt Bokeh Figure")

x = list(range(12))
y = [v**2 for v in x]

NUM_PLOTS = 3

# Define a DataSource
data = dict(x=[0]*NUM_PLOTS)

line_source = ColumnDataSource(data=data)

js = '''
var geometry = cb_data['geometry'];
console.log(geometry);
var data = line_source.data;
var x = data['x'];
console.log(x);
if (isFinite(geometry.x)) {
  for (i = 0; i < x.length; i++) {
    x[i] = geometry.x;
  }
  line_source.change.emit();
}
'''


plots = []
for i in range(NUM_PLOTS):
    plot = figure(plot_width=250, plot_height=250, title=None)
    plot.segment(x0='x', y0=0, x1='x', y1=200, color='red', line_width=1, source=line_source)
    plot.circle(x, y, size=10, color="navy", alpha=0.5)
    hover = HoverTool(tooltips=None, 
                      point_policy='follow_mouse', 
                      callback=CustomJS(code=js, args={'line_source': line_source}))
    plot.add_tools(hover)
    plots.append(plot)

show(column(*plots))
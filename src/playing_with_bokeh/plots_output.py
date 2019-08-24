"""
Return path to file in output file folder
"""
import pathlib


def plot_out(plot_name):
    """Os indenpendent path to a folder where plots are stored
    
    params:
        plot_name - name of the output plot taken to {name}.html 
    """
    name = "{}.html".format(plot_name)
    plot_path = pathlib.Path(__file__).resolve().parent.parent.parent
    plot_path = pathlib.Path.joinpath(plot_path, "plots")
    if not plot_path.exists():
        plot_path.mkdir(parents=True, exist_ok=True)
    return pathlib.Path.joinpath(plot_path, name)

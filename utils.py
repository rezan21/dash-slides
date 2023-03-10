# create plotly figure from json file
import json
from plotly import graph_objs as go

def load_json_as_fig(file_name):
    with open(f"./plots/{file_name}.json", "r") as file:
        data = json.load(file)
    return go.Figure(data)

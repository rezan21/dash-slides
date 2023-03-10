import json
from presentation import presentation_title
import dash
import dash_bootstrap_components as dbc
import pandas as pd

external_stylesheets = [dbc.themes.BOOTSTRAP, "./assets/custom.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
app.title = presentation_title
server = app.server

with open("./data/dd.json", "r") as f:
    dropdown_options = json.load(f)


with open("./data/recs.json", "r") as f:
    recs = json.load(f)

prods = pd.read_csv("./data/prods.csv")

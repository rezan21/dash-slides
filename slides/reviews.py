# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
from utils import load_json_as_fig


content = html.Div(
    style=dict(paddingLeft="100px"),
    children=[
        html.H2("EDA: Exploratory Data Analysis"),
        html.H3("Ratings"),
        dcc.Graph(id="rating_piecharts", figure=load_json_as_fig("rating_piecharts")),
        html.H3("Reviews - Sentiment Analysis"),
        dcc.Graph(id="sentiment", figure=load_json_as_fig("sentiment")),
        html.H3("Frequent Reviewers (min. 5 reviews)"),
        dcc.Graph(id="heatmap", figure=load_json_as_fig("heatmap")),
    ],
)

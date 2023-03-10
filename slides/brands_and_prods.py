# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
from utils import load_json_as_fig

content = html.Div(
    style=dict(paddingLeft="100px"),
    children=[
        # dcc.Markdown(
        #     """
        #     This is template content!
        #     """
        # ),
        # html.Li("a"),
        # html.Li("a"),
        # html.Li("a"),
        html.H2("EDA: Exploratory Data Analysis"),
        html.H3("Brands"),
        dcc.Graph(id="brand_stats", figure=load_json_as_fig("brand_stats")),
        html.H3("Products - Top-5"),
        dcc.Graph(id="top_prods", figure=load_json_as_fig("top_prods"), style=dict(width="100%")),
        html.H3("Products - All"),
        dcc.Graph(id="all_prods_treemap", figure=load_json_as_fig("all_prods_treemap"), style=dict(width="100%")),
    ],
)

# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app


content = html.Div(
    style=dict(paddingLeft="100px"),
    children=[
        html.H2("EDA: Exploratory Data Analysis"),
        html.H3("Ingredients"),
        html.Div(
            html.Img(
                src="assets/wordcloud.png",
                style=dict(width="1000px"),
            ),
            style=dict(textAlign="center"),
        ),
    ],
)

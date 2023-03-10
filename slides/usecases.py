# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app
from utils import load_json_as_fig


content = html.Div(
    html.Div(
        style=dict(paddingLeft="100px"),
        children=[
            html.H2("Use Cases:"),
            html.H3("1- Flavor/Product Recommendation System:"),
            html.H4(
                "Develop a recommendation system that suggests flavors for similar products or based on the user's preferences."
            ),
            html.Br(),
            html.H3("2- Ingredients Analysis & Flavour Generation:"),
            html.H4(
                "Identify the ingredients that are most liked by consumers and use this information to develop NEW flavors or modify existing ones."
            ),
            html.Br(),
            html.H3("3- Sentiment Analysis:"),
            html.H4(
                "Analyze the sentiment of reviews to identify any negative feedback and improve the overall product quality."
            ),
            html.Br(),
            html.H3("4- Sales Forecasting (data not provided):"),
            html.H4(
                "Develop a model to predict future sales based on historical data, weather patterns, and other external factors."
            ),
            html.Br(),
            html.H3("5- Image analysis (insufficient data):"),
            html.H4(
                "Use computer vision techniques to analyze the product images and identify any patterns or trends that can be used to improve sales or marketing."
            ),
            html.Br(),
        ],
    )
)

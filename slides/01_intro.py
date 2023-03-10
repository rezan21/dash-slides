# necessary imports - do not change
from dash import html, dcc, Input, Output, State
from server import app

content = html.Div(
    style=dict(textAlign="center"),
    children=[
        html.H1("The Sweet Science of Ice Cream"),
        html.H2("Uncovering Flavor Relationships"),
        html.H3("Reza N", className="t-light"),
        html.Br(),
        html.Div(
            html.Img(
                src="assets/ice-creams.jpg",
                style=dict(width="1000px", height="700px"),
            )
        ),
        # html.Div(
        #     style=dict(textAlign="left", marginLeft="40%"),
        #     children=[
        #         html.H2("Table of Contents:"),
        #         html.H3("EDA: Exploratory Data Analysis"),
        #         html.H4("Brands", style=dict(marginLeft="40px")),
        #         html.H4("Products", style=dict(marginLeft="40px")),
        #         html.H4("Reviews/Ratings", style=dict(marginLeft="40px")),
        #         html.H4("Ingredients", style=dict(marginLeft="40px")),
        #         html.H3("Use Cases"),
        #         html.H3("Prototype"),
        #         html.H3("Results (Justification)"),
        #     ],
        # ),
    ],
)

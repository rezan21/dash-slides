# necessary imports - do not change
from dash import html, dcc, Input, Output, State, dash_table
from server import app, dropdown_options, recs, prods
from utils import load_json_as_fig


content = html.Div(
    style=dict(paddingLeft="100px"),
    children=[
        html.H2("Prototype: Recommendation System"),
        dcc.Markdown(
            """
#### The system recommends ice-cream products to users based on the ingredients of one product that the user likes.
#### - Embedding: Represent each ice-cream product as a vector of numerical features that capture its ingredients. (OpenAI GPT3)
#### - Similarity: Find the most similar ice-cream products to the user's favorite product. (Cosine Similarity)
#### - Visualization: Visualize the embedding of the ice-cream products in 2D space. (t-SNE)
"""
        ),
        dcc.Graph(id="tsne", figure=load_json_as_fig("tsne")),
        dcc.Dropdown(id="dropdown-menu", options=dropdown_options, value="8_breyers"),
        dash_table.DataTable(id="result"),
    ],
)


@app.callback(Output("result", "data"), [Input("dropdown-menu", "value")])
def update_plot(prod):
    table = prods[prods["key"].isin(recs[prod])]
    return table.to_dict("records")

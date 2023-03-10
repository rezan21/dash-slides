# necessary imports - do not change
from dash import html, dcc, Input, Output, State, dash_table
from server import app, dropdown_options, recs, prods
from utils import load_json_as_fig


content = html.Div(
    style=dict(paddingLeft="100px"),
    children=[
        html.H2("Why Adopt this Recommendation System?"),
        dcc.Markdown(
            """
An ice cream startup should use my recommendation system for several reasons:

1. **Personalisation:** Allow users to receive personalised ice cream recommendations -> Increase customer satisfaction & loyalty.

2. **Efficiency:** Streamline the ice cream selection process - Finding similar flavors without having to spend time browsing -> Improve user experience & increase the likelihood of a sale.

3. **Scalability:** The system is designed to work with a large number of products - With new flavors or expand to new markets, the system will continue to provide accurate and relevant recommendations to users.

4. **Customer Insight:**  Tracking user preferences & improve marketing efforts, product development, and overall business strategy.

Overall, the recommendation system can help an ice cream startup to improve the **user experience**, increase **customer satisfaction and loyalty**, and **differentiate** itself from competitors.
By providing personalized and efficient ice cream recommendations, the system can help to **drive sales** and support the **growth** of the business.

"""
        ),
    ],
)

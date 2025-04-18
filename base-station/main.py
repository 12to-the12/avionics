from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly
from random import random

app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO])  # Choose your theme

# Create app layout shell
app.layout = html.Div(
    style={"padding": "2rem", "height": "100vh"},
    children=[
        html.Div(children="hello world!"),
        dcc.Graph(style={"height": "45%"}, id="altitude"),
        dcc.Graph(style={"height": "45%"}, id="acceleration"),
        dcc.Interval(id="interval-component", interval=1 * 500),
    ],
)


# # Multiple components can update everytime interval gets fired.
@callback(Output("altitude", "figure"), Input("interval-component", "n_intervals"))
def update_graph(n):
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=1)
    fig["layout"]["legend"] = {"x": 0, "y": 1, "xanchor": "left"}
    fig["layout"]["margin"] = {"l": 30, "r": 10, "b": 30, "t": 10}
    fig.append_trace(
        {
            "x": [2 * i for i in range(1_000)],
            "y": [i**0.5 * (1 + 0.1 * random()) for i in range(1_000)],
            "name": "Altitude",
            "mode": "lines+markers",
            "type": "scatter",
        },
        1,
        1,
    )
    return fig


# # Multiple components can update everytime interval gets fired.
@callback(Output("acceleration", "figure"), Input("interval-component", "n_intervals"))
def update_graph(n):
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=1)
    fig["layout"]["legend"] = {"x": 0, "y": 1, "xanchor": "left"}
    fig["layout"]["margin"] = {"l": 30, "r": 10, "b": 30, "t": 10}
    fig.append_trace(
        {
            "x": [2 * i for i in range(1_000)],
            "y": [i*(1 + 0.1 * random()) for i in range(1_000)],
            "name": "Altitude",
            "mode": "lines+markers",
            "type": "scatter",
        },
        1,
        1,
    )
    return fig


# Run the app if called
if __name__ == "__main__":
    app.run(debug=True)

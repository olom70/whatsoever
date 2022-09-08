import plotly.graph_objs as go
import pandas as pd
from importVIP import feedList
from dash import Dash, html, dcc

app = Dash(__name__)


size = []
name = []
parent = []
level = []
textinfo = []

parent, name, size, level, textinfo = feedList()


fig = go.Figure() 
fig.add_trace(go.Treemap( 
   labels = name, 
   parents = parent, 
   values = size,
   hovertext=textinfo 
))

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
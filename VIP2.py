import json
from anytree import PostOrderIter
from anytree.importer import DictImporter
import ipywidgets as widgets
import plotly.graph_objs as go
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from importVIP import feedList

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
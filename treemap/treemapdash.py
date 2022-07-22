import json
from anytree import PostOrderIter
from anytree.importer import DictImporter
import ipywidgets as widgets
import plotly.graph_objs as go
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

with open('flare.json') as f:
    js_data = json.loads(f.read())


importer = DictImporter()



root = importer.import_(js_data)

size = []
name = []
parent = []
level = []

def format(node):
    for i in node.children:
        if hasattr(i, 'value') == False:
            format(i)
        v = i.value
        if hasattr(i.parent, 'value'):
            i.parent.value += v
        elif hasattr(i.parent, 'value') == False:
            i.parent.value = v
        
        level.append(len(i.ancestors))
        name.append(i.name)
        parent.append(i.parent.name)
        size.append(i.value)

format(root)

level.append(0) 
name.append(root.name) 
parent.append("")
size.append(root.value)

fig = go.Figure() 
fig.add_trace(go.Treemap( 
   labels = name, 
   parents = parent, 
   values = size 
))#show figure 


app = Dash(__name__)

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
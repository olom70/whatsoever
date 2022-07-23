import json
from anytree import PostOrderIter
from anytree.importer import DictImporter
import ipywidgets as widgets
import plotly.graph_objs as go
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
from importVIP import feedList

size = []
ids = []
parent = []
level = []
textinfo = []
label = []

parent, ids, size, level, textinfo, label = feedList()


df = pd.DataFrame() 
df['parent'] = parent 
df['ids'] = ids 
#df['value']= size 
df['level'] = level
df['hovertext'] = textinfo
df['label'] = label


app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        0,
        3,
        step=None,
        value=3,
        marks = {0 : 'VIP', 1: 'Level1', 2: 'Level2', 3: 'Level3'},
        id='sliderVal'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('sliderVal', 'value'))
def update_figure(sliderVal):

    fig = go.Figure()
    fig.add_trace(go.Treemap(
        ids = df[df['level']<=sliderVal]['ids'],
        labels = df[df['level']<=sliderVal]['label'],
        #values = df[df['level']<=sliderVal]['value'],
        parents = df[df['level']<=sliderVal]['parent'],
        hovertext=df[df['level']<=sliderVal]['hovertext']
    ))
    fig.update_traces(root_color="#f1f1f1")
    fig.update_layout(width = 900, height = 900)


    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
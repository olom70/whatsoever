import json
from anytree import PostOrderIter
from anytree.importer import DictImporter
import ipywidgets as widgets
import plotly.graph_objs as go
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

with open('./treemap/flare.json') as f:
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

# fig = go.Figure() 
# fig.add_trace(go.Treemap( 
#    labels = name, 
#    parents = parent, 
#    values = size 
# ))#show figure 

df = pd.DataFrame() 
df['parent'] = parent 
df['name'] = name 
df['value']= size 
df['level'] = level


app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        0,
        5,
        step=None,
        value=5,
        id='sliderVal'
    )
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('sliderVal', 'value'))
def update_figure(sliderVal):

    fig = go.Figure()
    fig.add_trace(go.Treemap(
        labels = df[df['level']<sliderVal]['name'],
        values = df[df['level']<sliderVal]['value'],
        parents = df[df['level']<sliderVal]['parent']  
    ))
    fig.update_traces(root_color="#f1f1f1")
    fig.update_layout(width = 900, height = 900)


    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
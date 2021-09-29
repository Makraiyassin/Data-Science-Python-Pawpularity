import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import dash
from dash.dependencies import Input, Output
from dash import html, dcc
from plotly.tools import mpl_to_plotly
import plotly.express as px
matplotlib.use("Agg")

data = pd.read_csv('train.csv')

# print(data[(data['Subject Focus']==1) & (data['Pawpularity'] > 50)] )
# print(data[data["Pawpularity"] < 25])
# print(data[data["Pawpularity"] > 75])
# print(data['Pawpularity'].value_counts())

app = dash.Dash(__name__)

page_title = html.H1("Pawpularity Project!")

def image(id):
    return html.Img(src=app.get_asset_url(f'{id}.jpg'))

def first_graph():
    data['Count']=data['Pawpularity'].value_counts()
    data['Popularity']=data['Pawpularity']
    pop=data['Pawpularity'].value_counts()
    df = pd.concat([pop.index.to_series(), pop], axis=1, keys=['Popularity', 'Count'])
    fig = px.bar(df, x='Popularity', y='Count')
    return fig

app.layout = html.Div(
    children=[
        page_title,
        dcc.Graph(figure=first_graph()),
        dcc.Slider(
            id="slider", 
            min=0, 
            max=100, 
            step=1, 
            value=0,
            marks={ i : f"{i}" for i in range(101)}
        ),
        html.P(id="slider_display")
    ]
)

@app.callback(
    Output(component_id='slider_display', component_property='children'),
    [Input(component_id='slider', component_property='value')]
)
def display_slider_value(slider_value):
    message=f"slider value : {slider_value}"
    return message

if __name__ == "__main__":
    app.run_server(debug = True)
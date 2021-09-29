import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import dash
from dash.dependencies import Input, Output
from dash import html, dcc
# from plotly.tools import mpl_to_plotly
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
    fig = px.bar(data, x='Popularity', y='Count')
    return fig.show()

app.layout = html.Div(
    children=[
        page_title,
        first_graph()
    ]
)

if __name__ == "__main__":
    app.run_server(debug = True)
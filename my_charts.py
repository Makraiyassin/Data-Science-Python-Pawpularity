import plotly.express as px
import pandas as pd

def first_graph(data):
    data['Count']=data['Pawpularity'].value_counts()
    data['Popularity']=data['Pawpularity']
    pop=data['Pawpularity'].value_counts()
    df = pd.concat([pop.index.to_series(), pop], axis=1, keys=['Popularity', 'Count'])
    fig = px.bar(df, x='Popularity', y='Count')
    return fig

def pie_chart(df,title):
    fig = px.pie(df, values='Yes', names='Criterion', title=title)
    return fig



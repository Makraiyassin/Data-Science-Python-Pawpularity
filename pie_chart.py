import plotly.express as px

def pie_chart(df,title):
    fig = px.pie(df, values='Yes', names='Criterion', title=title)
    return fig



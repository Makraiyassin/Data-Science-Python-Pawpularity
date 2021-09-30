import pandas as pd
import matplotlib
import dash
from dash.dependencies import Input, Output
from dash import html, dcc
import plotly.express as px
from utils.data import data, df_populary, df_unpopulary
from my_charts import first_graph, pie_chart
matplotlib.use("Agg")

app = dash.Dash(__name__)

page_title = html.H1("Pawpularity Project!")
first_paragraph = html.P("This graphic groups the popularity ratings of over 9,900 animal photos.")
second_paragraph = html.P("The slider below allows you to display the photos according to their popularity. So we can find theories to explain their score.")

def get_image(id):
    return html.Img(src=app.get_asset_url(f'images/{id}.jpg'))

app.layout = html.Div(
    children=[
        page_title,
        first_paragraph,
        dcc.Graph(figure=first_graph(data)),
        second_paragraph,
        dcc.Slider(
            id="slider", 
            min=0, 
            max=100, 
            step=1, 
            value=0,
            marks={ i : f"{i}" for i in range(101)}
        ),
        html.Div(id="slider_display"),
        html.P("In the following graphs we will analyze the characteristics of popular photos and unpopular photos"),
        dcc.Graph(figure=pie_chart(df_populary, "most popular photos")),
        dcc.Graph(figure=pie_chart(df_unpopulary, "less popular photos")),
    ]
)

@app.callback(
    Output(component_id='slider_display', component_property='children'),
    [Input(component_id='slider', component_property='value')]
)
def display_slider_value(slider_value):
    if not slider_value == 0:
        pop = data[(data["Pawpularity"] < slider_value + 1) & (data["Pawpularity"] > slider_value - 1)]
        return html.Div(
            className="images",
            children=[get_image(id) for id in pop['Id']]
        )
    return 

if __name__ == "__main__":
    app.run_server(debug = True)
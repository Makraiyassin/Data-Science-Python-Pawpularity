import os
import matplotlib
import dash
from dash.dependencies import Input, Output
from dash import html, dcc
from utils.data import data, df_populary, df_unpopulary
from utils.my_charts import first_graph, pie_chart
from flask import Flask
matplotlib.use("Agg")

server = Flask(__name__)

app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/'
)

populary_chart=html.Div(
    className="pie-graph",
    children=[dcc.Graph(figure=pie_chart(df_populary,column,df_populary["Yes/No"], column)) for column in df_populary.columns if not column == "Yes/No"]
)
unpopulary_chart=html.Div(
    className="pie-graph",
    children=[dcc.Graph(figure=pie_chart(df_unpopulary,column,df_unpopulary["Yes/No"], column)) for column in df_unpopulary.columns if not column == "Yes/No"]
)

def get_image(id):
    return html.Img(src=app.get_asset_url(f'images/{id}.jpg'))

app.layout = html.Div(
    children=[
        html.H1("Pawpularity Project!"),
        html.P("This graphic groups the popularity ratings of over 9,900 animal photos."),
        dcc.Graph(figure=first_graph(data)),
        html.P("The slider below allows you to display the photos according to their popularity. So we can find theories to explain their score. 👇"),
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
        html.H1("Pie Charts for Most popular photos"),
        populary_chart,
        html.H1("Pie Charts for Less popular photos"),
        unpopulary_chart,
        html.P("When comparing the characteristics of the most popular photos with those of the less popular, there is no particular difference. The popularity of one over the other is subjective, it is difficult to make an algorithm allowing it to be calculated. We could possibly look at other characteristics, which could be more relevant such as: The brightness, the background, if the animal in the photo is an adult or a baby, ..."),
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

@server.route("/dash")
def my_dash_app():
    return app.index()

if __name__ == "__main__":
    server.run(debug = False, port=os.environ.get('PORT', 8080))
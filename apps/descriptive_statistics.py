#################### Libraries ####################
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import pathlib
from app import app
import plotly.io as pio
pio.templates.default = "plotly_dark"

#################### Data Path ####################
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

#################### Datasets ####################
skills_count = pd.read_csv(DATA_PATH.joinpath("./Skills Count.csv"))
weakfoot_count = pd.read_csv(DATA_PATH.joinpath("./Weakfoot Count.csv"))
height_count = pd.read_csv(DATA_PATH.joinpath("./Height Count.csv"))
weight_count = pd.read_csv(DATA_PATH.joinpath("./Weight Count.csv"))
workrate_count = pd.read_csv(DATA_PATH.joinpath("./Workrate Count.csv"))
league_count = pd.read_csv(DATA_PATH.joinpath("./League Count.csv"))
nation_count = pd.read_csv(DATA_PATH.joinpath("./Nation Count.csv"))
age_count = pd.read_csv(DATA_PATH.joinpath("./Age Count.csv"))
foot_count = pd.read_csv(DATA_PATH.joinpath("./Foot Count.csv"))
rating_count = pd.read_csv(DATA_PATH.joinpath("./Rating Count.csv"))
position_counts = pd.read_csv(DATA_PATH.joinpath("./Position Counts.csv"))
general_position_counts = pd.read_csv(DATA_PATH.joinpath("./General Position Counts.csv"))

#################### Layout ####################
layout = html.Div([


             html.Div(children = [html.H1("Descriptive Statistics"),
                                 html.P('''Here you are able to see descriptive statistics of FIFA Ultimate Team 2020, which includes counts of
                                 the features in the game.''')],
                                style = {'padding' : '10px' ,
                                         'backgroundColor' : '#e0e0e0',
                                         'text-align': 'center', 'whiteSpace': 'pre-wrap'
                                         }),

            html.Div(html.H2("Positional and Rating Counts"),
                    style = {'padding' : '0px' ,
                             'text-align': 'center',
                             'backgroundColor' : '#222831', 'display': 'inline-block', 'verticalAlign': 'top',
                              "width": "50%", "color": "white"
                             }),

            html.Div(html.H2("Player Nation and League Counts"),
                    style = {'padding' : '0px' ,
                             'text-align': 'center', "width": "50%",
                             'backgroundColor' : '#4e525a', 'display': 'inline-block', 'verticalAlign': 'top',
                             "color": "white"
                             }),

            html.Div([
                dcc.Dropdown(
                    id='position counts drop',
                    options=[
                        {'label': 'General Positions Counts', 'value': 'General Positions Counts'},
                        {'label': 'Position Counts', 'value': 'Position Counts'},
                        {'label': 'Rating Counts', 'value': 'Rating Counts'}
                    ],
                    value='General Positions Counts'
                )], style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

            html.Div([
                dcc.Dropdown(
                    id='nation and league info',
                    options=[
                        {'label': 'Player Nation', 'value': 'Player Nation'},
                        {'label': 'Player League', 'value': 'Player League'}
                    ],
                    value='Player Nation'
                )], style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

                  html.Div(
                          dcc.Graph(id = 'positions graph'),
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%", 'backgroundColor' : '#cde4e2'}),

                  html.Div(
                          dcc.Graph(id = 'nat and leg graph'),
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%", 'backgroundColor' : '#cde4e2'}),

            html.Div(
                                html.H2("Physical Player Information Counts"),
                                style = {'padding' : '0px' ,
                                         'text-align': 'center',
                                         'backgroundColor' : '#4e525a', 'width': '50%',
                                         'display': 'inline-block', 'verticalAlign': 'top', "color": "white"
                                         }),

            html.Div(
                                html.H2("In-Game Player Information Counts"),
                                style = {'padding' : '0px' ,
                                         'text-align': 'center', 'backgroundColor' : '#222831', 'width': '50%',
                                         'display': 'inline-block', 'verticalAlign': 'top', "color": "white"
                                         }),

            html.Div([
                dcc.Dropdown(
                    id='pysichal player info',
                    options=[
                        {'label': 'Age Counts', 'value': 'Age Counts'},
                        {'label': 'Height Counts', 'value': 'Height Counts'},
                        {'label': 'Weight Counts', 'value': 'Weight Counts'}
                    ],
                    value='Age Counts'
                )], style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

            html.Div([
                dcc.Dropdown(
                    id='in game player info',
                    options=[
                        {'label': 'Preferred Foot', 'value': 'Preferred Foot'},
                        {'label': 'Skill Moves', 'value': 'Skill Moves'},
                        {'label': 'Weakfoot', 'value': 'Weakfoot'},
                        {'label': 'Workrates', 'value': 'Workrates'}
                    ],
                    value='Preferred Foot'
                )], style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

                  html.Div(
                          dcc.Graph(id = 'phy'),
                          style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%", 'backgroundColor' : '#cde4e2'}),


                  html.Div(
                          dcc.Graph(id = 'in game player graph'),
                             style = {'display': 'inline-block', 'verticalAlign': 'top',  'padding':'0px', "width": "50%", 'backgroundColor' : '#cde4e2'})

])

#################### Callbacks ####################
@app.callback(Output('positions graph', 'figure'),
              [Input('position counts drop', 'value')])
def set_card_type_options(selected_value):
    if selected_value == 'General Positions Counts':
        data = [go.Pie(labels=general_position_counts["General Position"],
                                  values=general_position_counts["Counts"],
                                  textinfo='label+percent',
                                  textfont_size=11,
                                  hole=.3)]

        return {"data": data, "layout": go.Layout(
                            title={
                                    'text': "General Position Counts",
                                    'x':0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            paper_bgcolor='#222831',
                            showlegend=False, height = 550, template= "plotly_dark")}

    if selected_value == 'Position Counts':
        data = [go.Pie(labels=position_counts["Position"],
                                  values=position_counts["Counts"],
                                  textinfo='label+percent',
                                  textfont_size=11,
                                  hole=.3)]

        return {"data": data, "layout": go.Layout(
                                                title={
                                                        'text': "Position Counts",
                                                        'x':0.5,
                                                        'xanchor': 'center',
                                                        'yanchor': 'top'},
                                                     paper_bgcolor='#222831',
                                                     showlegend=False, height = 550, template= "plotly_dark")}
        return figure

    if selected_value == 'Rating Counts':
        figure = px.bar(rating_count,
                          x = "Rating",
                          y = "Counts",
                          color = "Counts",
                          color_continuous_scale=px.colors.diverging.RdYlGn,
                          title='Number of Players by Ratings').update(layout=dict(title=dict(x=0.5), paper_bgcolor='#222831', height = 550))
        return figure


@app.callback(Output('nat and leg graph', 'figure'),
              [Input('nation and league info', 'value')])
def set_card_type_options(selected_value):
    if selected_value == 'Player Nation':
        data = [go.Choropleth(
                              locations = nation_count['Nation'],
                              z = nation_count['Counts'],
                              colorscale = 'emrld',
                              locationmode='country names',
                              text = nation_count['Nation'],
                              autocolorscale=False,
                              reversescale=False,
                              marker_line_color='darkgray',
                              marker_line_width=0.5,
                              colorbar_title = 'Player Count')
                ]

        return {"data": data, "layout": go.Layout(
                            height = 550,
                            title={
                                    'text': "Count of Players by Country",
                                    'x':0.5,
                                    'xanchor': 'center',
                                    'yanchor': 'top'},
                            template= "plotly_dark",
                            paper_bgcolor="#4e525a",
                            coloraxis = {"colorbar": {"title": "Player Count",
                                                      "xpad": 0,
                                                      "ypad": 0
                                         }})
                                                    }

    if selected_value == 'Player League':
        figure = px.scatter(league_count,
                                      x = 'League',
                                      y = "Counts",
                                      size="Counts",
                                      color = "League",
                                      title='Number of Players by League').update(layout=dict(title=dict(x=0.5), paper_bgcolor="#4e525a",
                                                                                  showlegend = False,
                                                                                  height = 550))
        return figure


@app.callback(Output('phy', 'figure'),
              [Input('pysichal player info', 'value')])
def set_card_type_options(selected_value):
    if selected_value == 'Age Counts':
        figure = px.bar(age_count,
                  x = "Age",
                  y = "Counts",
                  title='Age Counts').update(layout=dict(title=dict(x=0.5), paper_bgcolor="#4e525a"))
        return figure

    if selected_value == 'Height Counts':
        figure = px.bar(height_count,
                                 x = 'Height(cm)',
                                 y = "Counts",
                                 title='Height Counts').update(layout=dict(title=dict(x=0.5), paper_bgcolor="#4e525a"))
        return figure

    if selected_value == 'Weight Counts':
        figure = px.bar(weight_count,
                          x = 'Weight(kg)',
                          y = "Counts",
                          title='Weight Counts').update(layout=dict(title=dict(x=0.5), paper_bgcolor="#4e525a"))
        return figure

@app.callback(Output('in game player graph', 'figure'),
              [Input('in game player info', 'value')])
def set_card_type_options(selected_value):
    if selected_value == 'Preferred Foot':
        figure = px.bar(foot_count,
                                  x = "Counts",
                                  y = "Foot",
                                  orientation = "h",
                                  color_discrete_sequence = ["green"],
                                  title='Preferred Foot').update(layout=dict(title=dict(x=0.5), paper_bgcolor='#222831'))
        return figure

    if selected_value == 'Skill Moves':
        figure = px.bar(skills_count,
                                  x = "Counts",
                                  y = "Skills",
                                  orientation = "h",
                                  color_discrete_sequence = ["blue"],
                                  title='Skill Moves'
                                  ).update(layout=dict(title=dict(x=0.5), paper_bgcolor='#222831'))
        return figure

    if selected_value == 'Weakfoot':
        figure = px.bar(weakfoot_count,
                                  x = "Counts",
                                  y = "Weakfoot",
                                  orientation = "h",
                                  color_discrete_sequence = ["red"],
                                  title='Weakfoot').update(layout=dict(title=dict(x=0.5), paper_bgcolor='#222831'))
        return figure


    if selected_value == 'Workrates':
        figure = px.bar(workrate_count,
                                  x = 'Counts',
                                  y = "Workrate",
                                  orientation = "h",
                                  color_discrete_sequence = ["orange"],
                                  title='Workrates').update(layout=dict(title=dict(x=0.5), paper_bgcolor='#222831'))
        return figure

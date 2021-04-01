#################### Libraries ####################
import dash
import dash_html_components as html
import pandas as pd
import dash_table
import warnings
warnings.filterwarnings("ignore")
import pathlib
from app import app

#################### Data Path ####################
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

#################### Datasets ####################
search_data= pd.read_csv(DATA_PATH.joinpath("./Search Data.csv"))

#################### Layout ####################
layout = html.Div([

            html.Div(children = [
                                  html.H1("Player Search Database"),
                                  html.P(['''In the Player Search Database you can search through any players in the game by filtering through every player attribute by scrolling to the right on the table.
                                                     ''', html.Br(),
                                                     '''If you want to see all the players with a Sprint Speed greater than 75 you would enter >75 into the filter and then press the ENTER key on your keyboard.''', html.Br(),
                                                     '''If you want to look for any player that has the Position Goalkeeper you would use the command GK into the filter then press ENTER on your keyboard.''', html.Br(), html.Br(),
                                                     '''If the value is numerical use the following math operations:''', html.Br(),
                                                     '''1. Greater Than: > 2. Less Than: < 3. Equal To: = 4. Greater Than or Equal To: >= 5. Less Than or Equal To: <='''])
                                     ],
                                style = {'padding' : '10px' ,
                                         'backgroundColor' : '#e0e0e0',
                                         'text-align': 'center', 'whiteSpace': 'pre-wrap'
                                         }),

            html.Div(dash_table.DataTable(
                                          id = 'table player search',
                                          columns=[{"name": i, "id": i} for i in search_data.columns],
                                          data=search_data.to_dict('records'),
                                          page_size=18,
                                          sort_action='native',
                                          filter_action='native',
                                          style_table={'overflowX': 'scroll'},
                                          style_as_list_view = False,
                                          style_data_conditional=[
                                                                    {
                                                                        'if': {'row_index': 'odd'},
                                                                        'backgroundColor': '#808080'
                                                                    }
                                                                ],
                                          style_header={'backgroundColor': '#4e525a',  'font-size': '12px', 'color': "white"},
                                          style_cell={'font-size': '12px', 'minWidth': '130px', 'width': '180px', 'maxWidth': '210px',
                                                     'textAlign': 'center',
                                                      'backgroundColor': '#C0C0C0',
                                                       'color': 'black'}
                                                            ),
                    style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%', 'padding':'0px', 'backgroundColor' : '#C0C0C0'})

        ])

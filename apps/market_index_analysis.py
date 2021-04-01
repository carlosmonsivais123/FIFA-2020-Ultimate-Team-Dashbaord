#################### Libraries ####################
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import dash_table
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
median_index_overtime = pd.read_csv(DATA_PATH.joinpath('./Median Index Overtime.csv'))
index_datatable = pd.read_csv(DATA_PATH.joinpath('./Index Data Table.csv'))
top_20_index = pd.read_csv(DATA_PATH.joinpath('./Top 20 Index.csv'))
bottom_20_index = pd.read_csv(DATA_PATH.joinpath('./Bottom 20 Index.csv'))
rating_indexes_ovt = pd.read_csv(DATA_PATH.joinpath('./Rating Index Overtime.csv'))
index_exploded = pd.read_csv(DATA_PATH.joinpath('./Index Exploded.csv'))

#################### Dropdown Dictionary ####################
rating_indexes_drop = []
for rating in rating_indexes_ovt["Rating"].unique():
    rating_indexes_drop.append({"label": str(rating), "value": rating})

#################### Color Based on Value ####################
color_gauge_list = []
if median_index_overtime["Indexes Overtime"].iat[-1] < 100:
    color_gauge_list.append("red")
else:
    color_gauge_list.append("green")

#################### Layout ####################
layout = html.Div([

            html.Div(children = [html.H1("Market Index Analysis"),
                                 html.P(['''The Market Index Analysis assigns an index that has been calculated to the market as whole through the change in players prices from one time period to another.''', html.Br(),
                                         '''The base index has been assigned using the initial prices which have been filtered and run through an algorithm to create the index.'''])],
                                style = {'padding' : '10px' ,
                                         'backgroundColor' : '#e0e0e0',
                                         'text-align': 'center', 'whiteSpace': 'pre-wrap'
                                         }),

            html.Div(dcc.Graph(id = "lowest gauge",
                              figure = {"data": [go.Indicator(
                                                                title = {"text": "Lowest Index", "font": {"color": "red"}},
                                                                mode = "number",
                                                                number = {"font": {"color": "red"}},
                                                                value = min(median_index_overtime["Indexes Overtime"]),
                                                                domain = {'x': [0, 1], 'y': [0, 1]})],
                                        "layout": go.Layout(height = 150,
                                                            margin = {"t":80, "b":20},
                                                            paper_bgcolor='#222831')
                                                                        }),
                      style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px'}
            ),

            html.Div(dcc.Graph(id = "market gauge",
                              figure = {"data": [go.Indicator(
                                                                title = {"text": "Current Index", "font": {"color": color_gauge_list[0]}},
                                                                mode = "number+delta",
                                                                number = {"font": {"color": color_gauge_list[0]}},
                                                                value = median_index_overtime["Indexes Overtime"].iat[-1],
                                                                delta = {'position': "bottom", 'reference': median_index_overtime["Indexes Overtime"].iat[-2]},
                                                                domain = {'x': [0, 1], 'y': [0, 1]})],
                                        "layout": go.Layout(height = 150,
                                                            margin = {"t":80, "b":20},
                                                            paper_bgcolor='#222831')
                                                                        }),
                      style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px'}
            ),

            html.Div(dcc.Graph(id = "highest gauge",
                              figure = {"data": [go.Indicator(
                                                                title = {"text": "Highest Index", "font": {"color": "green"}},
                                                                mode = "number",
                                                                number = {"font": {"color": "green"}},
                                                                value = max(median_index_overtime["Indexes Overtime"]),
                                                                domain = {'x': [0, 1], 'y': [0, 1]})],
                                        "layout": go.Layout(height = 150,
                                                            margin = {"t":80, "b":20},
                                                            paper_bgcolor='#222831')
                                                                        }),
                      style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px'}
            ),

            html.Div(dcc.Graph(figure = px.scatter(median_index_overtime, x="Dates Overtime",
                                                   y="Indexes Overtime", title = "<b>Index Over Time</b>",
                                                   color = "Indexes Overtime",
                                                   color_continuous_scale = px.colors.diverging.RdYlGn,
                                                   labels = {"Dates Overtime": "Date", "Indexes Overtime": "Index"}
                                                  ).update(layout=dict(title=dict(x=0.5, font =  {"color": "white", "size": 24, 'family': "Times New Roman"}), paper_bgcolor='#4e525a'))),
                      style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%', 'padding':'0px'}
            ),

            html.Div( html.H2("Player Search Index Values"),
                                style = {'padding' : '10px' ,
                                         'text-align': 'center',
                                         'backgroundColor' : '#222831', "color": "white"
                                         }),

            html.Div(dash_table.DataTable(
                                          id = 'table player index search',
                                          columns=[{"name": i, "id": i} for i in index_datatable.columns],
                                          data=index_datatable.to_dict('records'),
                                          page_size=10,
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
                                          style_header={'backgroundColor': '#4e525a', 'color': "white",  'font-size': '12px'},
                                          style_cell={'font-size': '12px', 'minWidth': '130px', 'width': '180px', 'maxWidth': '210px',
                                                     'textAlign': 'center',
                                                      'backgroundColor': '#C0C0C0',
                                                       'color': 'black'}
                                                            ),
                    style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%', 'padding':'0px', 'backgroundColor':'#C0C0C0'}),

            html.Div(html.H2("20 Lowest and Highest Indexes"),
                     style={'text-align':'center', "color": "white", 'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%',
                            'padding':'0px', 'backgroundColor':"#4e525a"}),

            html.Div(
                        dcc.Graph(id = "bottom 20 indexes",
                                  figure = {"data": [go.Table(columnwidth = [12, 27,25,11,11,13,13],
                                                              header=dict(values=["Number", "Name", "Card Type", "Rating", "Position",
                                                                                  "Current Index", "Current Price"],
                                                                          line_color='white',
                                                                          fill_color='#222831',
                                                                          font=dict(color='white', size=12),
                                                                          align='center'),
                                                              cells=dict(values=[(bottom_20_index.index+1), bottom_20_index.Name, bottom_20_index["Card Type"], bottom_20_index.Rating, bottom_20_index.Position,
                                                                                 bottom_20_index["Current Index"], bottom_20_index["Current Price"]],
                                                                         line_color='white',
                                                                         fill_color='#4e525a',
                                                                         font=dict(color='white', size=10),
                                                                         align='center'))],

                                            "layout": go.Layout(height = 520, paper_bgcolor='#4e525a', template= "plotly_dark",
                                                                title={
                                                                        'text': "20 Lowest Player Indexes",
                                                                        'x':0.5,
                                                                        'y': 0.97,
                                                                        'xanchor': 'center',
                                                                        'yanchor': 'top'},
                                                                margin = {"t":40, "b":20})}),
                                                                style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

            html.Div(
                        dcc.Graph(id = "top 20 indexes",
                                  figure = {"data": [go.Table(columnwidth = [12, 27,25,11,11,13,13],
                                                              header=dict(values=["Number", "Name", "Card Type", "Rating", "Position",
                                                                                  "Current Index", "Current Price"],
                                                                          line_color='white',
                                                                          fill_color='#222831',
                                                                          font=dict(color='white', size=12),
                                                                          align='center'),
                                                              cells=dict(values=[(top_20_index.index +1), top_20_index.Name, top_20_index["Card Type"], top_20_index.Rating, top_20_index.Position,
                                                                                 top_20_index["Current Index"], top_20_index["Current Price"]],
                                                                         line_color='white',
                                                                         fill_color='#4e525a',
                                                                         font=dict(color='white', size=10),
                                                                         align='center'))],

                                            "layout": go.Layout(height = 520, margin = {"t":40, "b":20}, paper_bgcolor='#4e525a', template= "plotly_dark",
                                                                title={
                                                                        'text': "20 Highest Player Indexes",
                                                                        'x':0.5,
                                                                        'y': 0.97,
                                                                        'xanchor': 'center',
                                                                        'yanchor': 'top'},
                                                                )}),
                                                                style={'display': 'inline-block', 'verticalAlign': 'top',
                                                                        'width': '50%', 'padding':'0px'}),

            html.Div(html.H2("Indexes by Categories: Rating, Card Type, League, Club"),
                     style={'text-align':'center', "color": "white", 'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%',
                            'padding':'0px', 'backgroundColor':"#222831"}),

            html.Div([
                dcc.Dropdown(
                    id='all index labels',
                    options=[
                        {'label': 'Rating', 'value': 'Rating'},
                        {'label': 'Card Type', 'value': 'Card Type'},
                        {'label': 'League', 'value': 'League'},
                        {'label': 'Club', 'value': 'Club'}
                    ],
                    value='Rating'
                )], style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "subset index labels",
                                 options= rating_indexes_drop,
                                 value= rating_indexes_ovt["Rating"][0],
                                 placeholder = "Select a Category"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '50%', 'padding':'0px'}),

            html.Div(
                    dcc.Graph(id = "all indexes graph"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%', 'padding':'0px'})

])

#################### Callbacks ####################
@app.callback(Output('subset index labels', 'options'),
              [Input('all index labels', 'value')])
def price_filter1(selected_value):
    newindex_exploded = index_exploded[[selected_value, 'Dates Overtime', 'Indexes Overtime']]
    newindex_exploded.reset_index(inplace = True, drop = True)
    league_indexes_ovt = pd.DataFrame(newindex_exploded.groupby([selected_value, 'Dates Overtime'])['Indexes Overtime'].median())
    league_indexes_ovt.reset_index(inplace = True, drop = False)
    league_indexes_ovt['Dates Overtime'] = league_indexes_ovt['Dates Overtime'].astype('datetime64[ns]')
    league_indexes_drop = []
    for league in league_indexes_ovt[selected_value].unique():
        league_indexes_drop.append({"label": str(league), "value": league})
    return league_indexes_drop

@app.callback(Output("all indexes graph", 'figure'),
              [Input('subset index labels', 'value'),
              Input('all index labels', 'value')])
def set_card_type_options(selected_value, selected_value2):
    newindex_exploded = index_exploded[[selected_value2, 'Dates Overtime', 'Indexes Overtime']]
    newindex_exploded.reset_index(inplace = True, drop = True)
    league_indexes_ovt = pd.DataFrame(newindex_exploded.groupby([selected_value2, 'Dates Overtime'])['Indexes Overtime'].median())
    league_indexes_ovt.reset_index(inplace = True, drop = False)
    league_indexes_ovt['Dates Overtime'] = league_indexes_ovt['Dates Overtime'].astype('datetime64[ns]')

    filtered_df = league_indexes_ovt[league_indexes_ovt[selected_value2] == selected_value]
    filtered_df.reset_index(drop = True, inplace = True)

    x_axis = filtered_df['Dates Overtime']
    y_axis = filtered_df['Indexes Overtime']

    data = [go.Scatter(
            x = x_axis,
            y = y_axis,
            marker_color=filtered_df['Indexes Overtime'],
            mode = 'markers',
            opacity = 0.6,
            marker = {"size": 6, 'colorscale': px.colors.diverging.RdYlGn, 'showscale': True, 'colorbar':{'title':"Index"}}
            )
            ]

    return {"data": data, "layout": go.Layout(title={"text": "{} Index Over Time".format(selected_value),
                                                    'x':0.5,
                                                    'xanchor': 'center',
                                                    'yanchor': 'top'},
                                                xaxis = {"title": "Date", "tickfont": {"size": 10}},
                                                paper_bgcolor = '#222831',
                                                template= "plotly_dark",
                                                yaxis = {"title": "Index", "tickfont": {"size": 10}},
                                                height =  600,
                                                margin = {"l": 80, "r": 80, "b": 80, "t":30})
                                                }

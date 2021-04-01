#################### Libraries ####################
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
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
median_index_overtime = pd.read_csv(DATA_PATH.joinpath('./Median Index Overtime.csv'))
dis = pd.read_csv(DATA_PATH.joinpath("./dis.csv"))
index_creation = pd.read_csv(DATA_PATH.joinpath('./Index Creation.csv'))

#################### Dropdown Dictionary ####################
player_name = []
for player in dis["Name"].unique():
    player_name.append({"label": str(player), "value": player})

card_type = []
for card in dis["Card Type"].unique():
    card_type.append({"label": str(card), "value": card})

rating_type = []
for rating in dis["Rating"].unique():
    rating_type.append({"label": str(rating), "value": rating})

position_type = []
for position in dis["Position"].unique():
    position_type.append({"label": str(position), "value": position})

club_type = []
for club in dis["Club"].unique():
    club_type.append({"label": str(club), "value": club})

nation_name = []
for nation in dis["Nation"].unique():
    nation_name.append({"label": str(nation), "value": nation})

league_name = []
for league in dis["League"].unique():
    league_name.append({"label": str(league), "value": league})

#################### Layout ####################
layout = html.Div([

            html.Div(children = [
                                html.H1("Player Information"),
                                html.P('''On the Player Information page, we are able to search any player in the game along with all their player cards.''')
                                     ],
                                style = {'padding' : '10px' ,
                                         'backgroundColor' : '#e0e0e0',
                                         'text-align': 'center', 'whiteSpace': 'pre-wrap'
                                         }),

            html.Div(
                    dcc.Dropdown(id = "player name",
                                 options= player_name,
                                 value= dis["Name"][1700],
                                 placeholder = "Select a Player"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '28%',
                                         'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "card type",
                                 options= card_type,
                                 value= dis["Card Type"][1700],
                                 placeholder = "Select a Card Type"
                                 ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "rating type",
                                 options= rating_type,
                                 value= dis["Rating"][1700],
                                 placeholder = "Select a Rating Value"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "position type",
                                 options= position_type,
                                 value= dis["Position"][1700],
                                 placeholder = "Select a Position"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "nation type",
                                 options= nation_name,
                                 value= dis["Nation"][1700],
                                 placeholder = "Select a Nation"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "league type",
                                 options= league_name,
                                 value= dis["League"][1700],
                                 placeholder = "Select a League"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "club type",
                                 options= club_type,
                                 value= dis["Club"][1700],
                                 placeholder = "Select a Club"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "name text")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '28%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "card text")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "rating text")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "position text")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "nation text")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "league text")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),


            html.Div([
                    html.H1(id = "team text")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),


            html.Div(
                    dcc.Graph(id = "information_table"),
                              style = {'margin': 'auto', 'width': '100%', 'backgroundColor' : '#dde7ee'}
                                    ),

            html.Div(
                    dcc.Graph(id = "pace_table"),
                              style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '16.66%', 'padding':'0px', 'backgroundColor' : '#dde7ee'}
                                    ),

            html.Div(
                    dcc.Graph(id = "shooting_table"),
                              style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '16.66%', 'padding':'0px', 'backgroundColor' : '#dde7ee'}
                                    ),

            html.Div(
                    dcc.Graph(id = "passing_table"),
                              style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '16.66%', 'padding':'0px', 'backgroundColor' : '#dde7ee'}
                                    ),

            html.Div(
                    dcc.Graph(id = "dribbling_table"),
                              style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '16.66%', 'padding':'0px', 'backgroundColor' : '#dde7ee'}
                                    ),

            html.Div(
                    dcc.Graph(id = "defending_table"),
                              style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '16.66%', 'padding':'0px', 'backgroundColor' : '#dde7ee'}
                                    ),

            html.Div(
                    dcc.Graph(id = "physical_table"),
                              style = {'display': 'inline-block', 'verticalAlign': 'top', 'width': '16.66%', 'padding':'0px', 'backgroundColor' : '#dde7ee'}
                                    ),

            html.Div(
                    dcc.Graph(id = 'graph-polar'),
                              style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'backgroundColor' : '#cde4e2'}
                                    ),

            html.Div([
                    dcc.Graph(id = 'price scatter')
            ], style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px', 'backgroundColor' : '#cde4e2'}),


            html.Div([
                      dcc.Graph(id = 'player index graph')
            ], style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '33.33%', 'padding':'0px', 'backgroundColor' : '#cde4e2'})
])

#################### Callbacks ####################
@app.callback(Output('card type', 'options'),
              [Input('player name', 'value')])
def price_filter1(selected_player):
    filtered_df = dis[dis["Name"] == selected_player]
    filtered_df.reset_index(drop = True, inplace = True)
    card_type = []
    for card in filtered_df["Card Type"].unique():
        card_type.append({"label": str(card), "value": card})
    return card_type

@app.callback(Output('rating type', 'options'),
              [Input('player name', 'value'),
               Input('card type', 'value')])
def price_filter1(selected_player, selected_card):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card)]
    filtered_df.reset_index(drop = True, inplace = True)
    rating_type = []
    for rating in filtered_df["Rating"].unique():
        rating_type.append({"label": str(rating), "value": rating})
    return rating_type

@app.callback(Output('position type', 'options'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value')])
def price_filter1(selected_player, selected_card, selected_rating):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating)]
    filtered_df.reset_index(drop = True, inplace = True)
    position_type = []
    for position in filtered_df["Position"].unique():
        position_type.append({"label": str(position), "value": position})
    return position_type

@app.callback(Output('nation type', 'options'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value')])
def price_filter1(selected_player, selected_card, selected_rating, selected_position):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position)]
    filtered_df.reset_index(drop = True, inplace = True)
    nation_name = []
    for nation in filtered_df["Nation"].unique():
        nation_name.append({"label": str(nation), "value": nation})
    return nation_name

@app.callback(Output('league type', 'options'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value')])
def price_filter1(selected_player, selected_card, selected_rating, selected_position, selected_nation):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation)]
    filtered_df.reset_index(drop = True, inplace = True)
    league_name = []
    for league in filtered_df["League"].unique():
        league_name.append({"label": str(league), "value": league})
    return league_name

@app.callback(Output('club type', 'options'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value')])
def price_filter1(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league)]
    filtered_df.reset_index(drop = True, inplace = True)
    club_type = []
    for club in filtered_df["Club"].unique():
        club_type.append({"label": str(club), "value": club})
    return club_type

@app.callback([Output('name text', 'children'),
               Output('card text', 'children'),
               Output('rating text', 'children'),
               Output('position text', 'children'),
               Output('nation text', 'children'),
               Output('league text', 'children'),
               Output('team text', 'children')],
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    filtered_df.reset_index(drop = True, inplace = True)

    children1 = filtered_df["Name"]
    children2 = filtered_df["Card Type"]
    children3 = filtered_df["Rating"]
    children4 = filtered_df["Position"]
    children5 = filtered_df["Nation"]
    children6 = filtered_df["League"]
    children7 = filtered_df["Club"]

    return children1, children2, children3, children4, children5, children6, children7


@app.callback(Output('price scatter', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    filtered_df.reset_index(drop = True, inplace = True)

    for player in filtered_df:
        x_axis = eval(filtered_df['Price Date'][0])
        x_axis = [w[:-13] for w in x_axis]
        y_axis = eval(filtered_df['Prices'][0])

        data = [go.Scatter(
                x = x_axis,
                y = y_axis,
                mode = 'lines+markers',
                line=dict(color='#cd00cd'),
                opacity = 0.4,
                marker = {"size": 6}
                )
                ]
        return {"data": data, "layout": go.Layout(title={'text': "Price History: {} {} {} {}".format(selected_player, selected_card, selected_rating, selected_position),
                                                        'x':0.5,
                                                        'xanchor': 'center',
                                                        'yanchor': 'top'},
                                                    xaxis = {"title": "Date", "tickfont": {"size": 10}},
                                                    yaxis = {"title": "Price", "tickfont": {"size": 10}},
                                                    template= "plotly_dark",
                                                    paper_bgcolor='#222831',
                                                    legend=dict(orientation = "h",
                                                                yanchor="top",
                                                                xanchor="center",
                                                                x=0.5,
                                                                y = 1.11
                                                            ),
                                                    margin = {"l": 80, "r": 80, "b": 80, "t":80})}

@app.callback(Output('player index graph', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = index_creation[(index_creation["Name"] == selected_player) & (index_creation["Card Type"] == selected_card) & (index_creation["Rating"] == selected_rating) & (index_creation["Position"] == selected_position) & (index_creation["Nation"] == selected_nation) & (index_creation["League"] == selected_league) & (index_creation["Club"] == selected_club)]
    filtered_df.reset_index(drop = True, inplace = True)

    for player in filtered_df:
        x_axis = eval(filtered_df['Price Date'][0])
        x_axis = [w[:-13] for w in x_axis]
        y_axis = eval(filtered_df['Price Indexes'][0])

        data = [go.Scatter(
                x = x_axis,
                y = y_axis,
                mode = 'lines+markers',
                line=dict(color='#00FF00'),
                opacity = 0.4,
                marker = {"size": 6}
                )]

        return {"data": data, "layout": go.Layout(title={"text": "Price Index: {} {} {} {}".format(selected_player, selected_card, selected_rating, selected_position),
                                                         'x':0.5,
                                                         'xanchor': 'center',
                                                         'yanchor': 'top'},
                                                    xaxis = {"title": "Date", "tickfont": {"size": 10}},
                                                    paper_bgcolor = '#222831',
                                                    template= "plotly_dark",
                                                    yaxis = {"title": "Price", "tickfont": {"size": 10}},
                                                    margin = {"l": 80, "r": 80, "b": 80, "t":80})}

# Polar Graph
@app.callback(Output('graph-polar', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    filtered_df.reset_index(drop = True, inplace = True)
    filtered_df = filtered_df[["PAC", "SHO", "DEF", "PAS", "PHY", "DRI", "PAC"]]
    filtered_df = filtered_df.loc[:,~filtered_df.columns.duplicated()]
    filtered_df = pd.DataFrame(filtered_df)
    filtered_df.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Barpolar(
            r = list(filtered_df.iloc[0]),
            theta = filtered_df.columns,
            marker_line_color="black",
            marker_line_width=2,
            opacity=0.5,
            marker_color=['#800080', '#0000FF', '#008000', '#FFFF00', '#FF0000', '#808080']
        ))
    return {"data": traces, "layout": go.Layout(title={'text': "{} {} {} {} Polar Graph".format(selected_player, selected_card, selected_rating, selected_position),
                                                    'x':0.5,
                                                    'xanchor': 'center',
                                                    'yanchor': 'top'},
                                                margin = {"l": 80, "r": 80, "b": 20, "t": 80}, paper_bgcolor='#222831', template= "plotly_dark",
                                                polar = dict(radialaxis = dict(range=[0, 99]),
                                                    ))}

# Player information_table
@app.callback(Output('information_table', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def player_info_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    index_list = list(filtered_df.index)
    pace_table = filtered_df[["Skills", "Weakfoot", "Age", "Height(cm)", "Weight(kg)", 'Workrate', 'Foot', 'League', 'Total Stats']]
    pace_table = pace_table.loc[:,~pace_table.columns.duplicated()]
    pace_table.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Table(
                header=dict(values=list(pace_table.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[pace_table["Skills"], pace_table["Weakfoot"], pace_table["Age"], pace_table["Height(cm)"], pace_table["Weight(kg)"],
                                    pace_table["Workrate"], pace_table["Foot"], pace_table["League"], pace_table["Total Stats"]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center')))

    return {"data": traces, "layout": go.Layout(height = 150,
                                                title = "{} {} {} {} Player Statistics".format(selected_player, selected_card, selected_rating, selected_position),
                                                title_font_color="white",
                                                paper_bgcolor='#4e525a', margin = {"l": 80, "r": 80, "b": 10, "t": 80})}

# Pace
@app.callback(Output('pace_table', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    index_list = list(filtered_df.index)
    pace_table = filtered_df[["PAC", "Acceleration", "Sprint Speed"]]
    pace_table = pace_table.loc[:,~pace_table.columns.duplicated()]
    pace_table = pace_table.T
    pace_table.reset_index(inplace = True, drop = False)
    pace_table = pace_table.rename(columns=pace_table.iloc[0]).drop(pace_table.index[0])
    pace_table.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Table(
                header=dict(values=list(pace_table.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[pace_table[pace_table.columns[0]], pace_table[pace_table.columns[1]]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center'))

        )
    return {"data": traces, "layout": go.Layout(height =  185, paper_bgcolor='#4e525a', margin = {"l": 80, "r": 0, "b": 0, "t": 20})}

# Shooting
@app.callback(Output('shooting_table', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    index_list = list(filtered_df.index)
    pace_table = filtered_df[["SHO", "Positioning", "Finishing", "Shot Power", "Long Shots", "Volleys", "Penalties"]]
    pace_table = pace_table.loc[:,~pace_table.columns.duplicated()]
    pace_table = pace_table.T
    pace_table.reset_index(inplace = True, drop = False)
    pace_table = pace_table.rename(columns=pace_table.iloc[0]).drop(pace_table.index[0])
    pace_table.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Table(
                header=dict(values=list(pace_table.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[pace_table[pace_table.columns[0]], pace_table[pace_table.columns[1]]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center'))

        )
    return {"data": traces, "layout": go.Layout(height =  185, paper_bgcolor='#4e525a', margin = {"l": 10, "r": 0, "b": 0, "t": 20})}

# Passing
@app.callback(Output('passing_table', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    index_list = list(filtered_df.index)
    pace_table = filtered_df[['PAS', 'Vision', 'Crossing', 'FK.Acc.', 'Short Pass', 'Long Pass', 'Curve']]
    pace_table = pace_table.loc[:,~pace_table.columns.duplicated()]
    pace_table = pace_table.T
    pace_table.reset_index(inplace = True, drop = False)
    pace_table = pace_table.rename(columns=pace_table.iloc[0]).drop(pace_table.index[0])
    pace_table.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Table(
                header=dict(values=list(pace_table.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[pace_table[pace_table.columns[0]], pace_table[pace_table.columns[1]]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center'))

        )
    return {"data": traces, "layout": go.Layout(height =  185, paper_bgcolor='#4e525a', margin = {"l": 10, "r": 0, "b": 0, "t": 20})}

# Dribbling
@app.callback(Output('dribbling_table', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    index_list = list(filtered_df.index)
    pace_table = filtered_df[['DRI', 'Agility', 'Balance', 'Reactions', 'Ball Control', 'Dribbling', 'Composure']]
    pace_table = pace_table.loc[:,~pace_table.columns.duplicated()]
    pace_table = pace_table.T
    pace_table.reset_index(inplace = True, drop = False)
    pace_table = pace_table.rename(columns=pace_table.iloc[0]).drop(pace_table.index[0])
    pace_table.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Table(
                header=dict(values=list(pace_table.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[pace_table[pace_table.columns[0]], pace_table[pace_table.columns[1]]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center'))

        )
    return {"data": traces, "layout": go.Layout(height =  185, paper_bgcolor='#4e525a', margin = {"l": 10, "r": 0, "b": 0, "t": 20})}

# Defending
@app.callback(Output('defending_table', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    index_list = list(filtered_df.index)
    pace_table = filtered_df[['DEF', 'Interceptions', 'Heading Acc.', 'Def. Awareness', 'Stand Tackle', 'Slide Tackle']]
    pace_table = pace_table.loc[:,~pace_table.columns.duplicated()]
    pace_table = pace_table.T
    pace_table.reset_index(inplace = True, drop = False)
    pace_table = pace_table.rename(columns=pace_table.iloc[0]).drop(pace_table.index[0])
    pace_table.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Table(
                header=dict(values=list(pace_table.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[pace_table[pace_table.columns[0]], pace_table[pace_table.columns[1]]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center'))

        )
    return {"data": traces, "layout": go.Layout(height =  185, paper_bgcolor='#4e525a', margin = {"l": 10, "r": 0, "b": 0, "t": 20})}

# Physical
@app.callback(Output('physical_table', 'figure'),
              [Input('player name', 'value'),
               Input('card type', 'value'),
               Input('rating type', 'value'),
               Input('position type', 'value'),
               Input('nation type', 'value'),
               Input('league type', 'value'),
               Input('club type', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]
    index_list = list(filtered_df.index)
    pace_table = filtered_df[['PHY', 'Jumping', 'Stamina', 'Strength', 'Aggression']]
    pace_table = pace_table.loc[:,~pace_table.columns.duplicated()]
    pace_table = pace_table.T
    pace_table.reset_index(inplace = True, drop = False)
    pace_table = pace_table.rename(columns=pace_table.iloc[0]).drop(pace_table.index[0])
    pace_table.reset_index(inplace = True, drop = True)
    traces = []

    traces.append(go.Table(
                header=dict(values=list(pace_table.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[pace_table[pace_table.columns[0]], pace_table[pace_table.columns[1]]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center'))

        )
    return {"data": traces, "layout": go.Layout(height =  185, paper_bgcolor='#4e525a', margin = {"l": 10, "r": 80, "b": 0, "t": 20})}

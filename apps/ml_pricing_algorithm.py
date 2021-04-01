#################### Libraries ####################
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import sklearn
import datetime
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

preds_list = []
for value in list(range(1, 31)):
    preds_list.append({"label": str(value), "value": value})

#################### Price Prediction Algorithm ####################
stored_preds = []
def linear_regression(player_pick, number_of_iters):
    stored_preds.clear()
    i = 0
    data = pd.Series(player_pick["Prices"])
    data.reset_index(inplace = True, drop = True)
    data = data.iloc[0]
    data = eval(data)
    data = pd.DataFrame(list(zip(data)), columns = ["Prices"])
    data_2 = pd.Series(player_pick["Price Date"])
    data_2.reset_index(inplace = True, drop = True)
    data_2 = data_2.iloc[0]
    data_2 = eval(data_2)
    data_2 = pd.DataFrame(list(zip(data_2)), columns = ["Date"])
    data_original = pd.merge(data, data_2, left_index = True, right_index = True)
    data_original['Date'] = pd.to_datetime(data_original['Date'])
    data_original['Day of the Week'] = data_original['Date'].dt.day_name()
    data_original['Date'] = data_original['Date'].dt.date
    data_original["Days on Market"] = data_original.index + 1
    data_original['MA1'] = data_original["Prices"].rolling(window=1).median()
    data_original['MA2'] = data_original["Prices"].rolling(window=2).median()
    data_original['Next Price'] = data_original['Prices'].shift(-1)
    data_drop_na = data_original.dropna()
    X = data_drop_na[["Day of the Week","Days on Market", "MA1", "MA2"]]
    Y = data_drop_na['Next Price']
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import OneHotEncoder
    num_attribs = ["Days on Market", "MA1", "MA2"]
    cat_attribs = ['Day of the Week']
    num_pipeline = Pipeline([
        ('std_scaler', StandardScaler())
    ])
    full_pipeline = ColumnTransformer([
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs)
    ])
    X_prepared = full_pipeline.fit_transform(X)
    from sklearn.linear_model import LinearRegression
    lin_reg = LinearRegression()
    from sklearn.model_selection import GridSearchCV
    parameters = {'fit_intercept': [True, False], 'normalize': [True, False], 'copy_X':[True, False]}

    grid_search = GridSearchCV(estimator = lin_reg,
                               param_grid = parameters,
                               scoring = 'neg_root_mean_squared_error',
                               cv = 3)
    grid_search.fit(X = X_prepared, y = Y)
    grid_search.best_params_.values()
    X_input = [X_prepared[-1]]
    y_pred = grid_search.predict(X_input)[0]
    stored_preds.append(y_pred)

    while i < number_of_iters:
        y_preds_dataframe = pd.DataFrame([stored_preds[i]])
        y_preds_dataframe.columns = ["Prices"]
        data_original = pd.concat([data_original, y_preds_dataframe])
        data_original.reset_index(inplace = True, drop = True)
        dates = list(pd.to_datetime(data_original["Date"]))
        import datetime
        new_dates = dates[:-1] + [(dates[-2] + datetime.timedelta(days= 1))]
        data_original['MA1'] = data_original["Prices"].rolling(window=1).median()
        data_original['MA2'] = data_original["Prices"].rolling(window=2).median()
        data_original['Next Price'] = data_original['Prices'].shift(-1)
        data_original['Date'] = new_dates
        data_original['Day of the Week'] = data_original['Date'].dt.day_name()
        data_original['Date'] = data_original['Date'].dt.date
        data_original["Days on Market"] = data_original.index + 1
        data_new = data_original.dropna()
        X = data_new[["Day of the Week", "Days on Market", "MA1", "MA2"]]
        Y = data_new['Next Price']
        X_prepared = full_pipeline.fit_transform(X)
        X_input = [X_prepared[-1]]
        y_pred = grid_search.predict(X_input)[0]
        stored_preds.append(y_pred)
        i = i + 1

    return data_original

#################### Layout ####################
layout = html.Div([
            html.Div(children = [
                                html.H1("Player Price Prediction"),

                                html.P(['''Any player's price can be searched up with a range between 1 and 30 days into the future along with a daily price breakdown displayed as a table.''', html.Br(),
                                        '''Keep in mind that the farther in the future that prices are predicted, the less accurate they become.'''])
                                     ],
                                style = {'padding' : '10px' ,
                                         'backgroundColor' : '#e0e0e0',
                                         'text-align': 'center'
                                         }),


            html.Div(
                    dcc.Dropdown(id = "player name 2",
                                 options= player_name,
                                 value= dis["Name"][1700],
                                 placeholder = "Select a Player"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '28%',
                                         'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "card type 2",
                                 options= card_type,
                                 value= dis["Card Type"][1700],
                                 placeholder = "Select a Card Type"
                                 ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "rating type 2",
                                 options= rating_type,
                                 value= dis["Rating"][1700],
                                 placeholder = "Select a Rating Value"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "position type 2",
                                 options= position_type,
                                 value= dis["Position"][1700],
                                 placeholder = "Select a Position"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "nation type 2",
                                 options= nation_name,
                                 value= dis["Nation"][1700],
                                 placeholder = "Select a Nation"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div(
                    dcc.Dropdown(id = "league type 2",
                                 options= league_name,
                                 value= dis["League"][1700],
                                 placeholder = "Select a League"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),


            html.Div(
                    dcc.Dropdown(id = "club type 2",
                                 options= club_type,
                                 value= dis["Club"][1700],
                                 placeholder = "Select a Club"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "name text 2")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '28%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "card text 2")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "rating text 2")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "position text 2")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "nation text 2")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "league text 2")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),

            html.Div([
                    html.H1(id = "team text 2")
            ], style={'backgroundColor':"#222831", 'color': 'white', 'fontSize': 10, 'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '12%', 'padding':'0px'}),


            html.Div([
                                html.H3("Number of Days to Predict")
                                     ],
                                style = {'padding' : '10px' ,
                                         'backgroundColor' : '#4e525a',
                                         'color': 'white',
                                         'text-align': 'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%', 'padding':'0px'
                                         }),

            html.Div(
                    dcc.Dropdown(id = "Days Predicted",
                                 options= preds_list,
                                 value= 1,
                                 placeholder = "Select the Number of Days"
                                ), style={'text-align':'center', 'display': 'inline-block', 'verticalAlign': 'top', 'width': '100%', 'padding':'0px'}),

            html.Div([
                      dcc.Graph(id = 'player predict price')
            ], style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '70%', 'padding':'0px', 'backgroundColor' : '#cde4e2'}),

            html.Div([
                      dcc.Graph(id = 'player predict price table')
            ], style={'display': 'inline-block', 'verticalAlign': 'top', 'width': '30%', 'padding':'0px', 'backgroundColor' : '#cde4e2'})
])

#################### Callbacks ####################
@app.callback(Output('card type 2', 'options'),
              [Input('player name 2', 'value')])
def price_filter1(selected_player):
    filtered_df = dis[dis["Name"] == selected_player]
    filtered_df.reset_index(drop = True, inplace = True)
    card_type = []
    for card in filtered_df["Card Type"].unique():
        card_type.append({"label": str(card), "value": card})
    return card_type

@app.callback(Output('rating type 2', 'options'),
              [Input('player name 2', 'value'),
               Input('card type 2', 'value')])
def price_filter1(selected_player, selected_card):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card)]
    filtered_df.reset_index(drop = True, inplace = True)
    rating_type = []
    for rating in filtered_df["Rating"].unique():
        rating_type.append({"label": str(rating), "value": rating})
    return rating_type

@app.callback(Output('position type 2', 'options'),
              [Input('player name 2', 'value'),
               Input('card type 2', 'value'),
               Input('rating type 2', 'value')])
def price_filter1(selected_player, selected_card, selected_rating):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating)]
    filtered_df.reset_index(drop = True, inplace = True)
    position_type = []
    for position in filtered_df["Position"].unique():
        position_type.append({"label": str(position), "value": position})
    return position_type

@app.callback(Output('nation type 2', 'options'),
              [Input('player name 2', 'value'),
               Input('card type 2', 'value'),
               Input('rating type 2', 'value'),
               Input('position type 2', 'value')])
def price_filter1(selected_player, selected_card, selected_rating, selected_position):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position)]
    filtered_df.reset_index(drop = True, inplace = True)
    nation_name = []
    for nation in filtered_df["Nation"].unique():
        nation_name.append({"label": str(nation), "value": nation})
    return nation_name

@app.callback(Output('league type 2', 'options'),
              [Input('player name 2', 'value'),
               Input('card type 2', 'value'),
               Input('rating type 2', 'value'),
               Input('position type 2', 'value'),
               Input('nation type 2', 'value')])
def price_filter1(selected_player, selected_card, selected_rating, selected_position, selected_nation):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation)]
    filtered_df.reset_index(drop = True, inplace = True)
    league_name = []
    for league in filtered_df["League"].unique():
        league_name.append({"label": str(league), "value": league})
    return league_name

@app.callback(Output('club type 2', 'options'),
              [Input('player name 2', 'value'),
               Input('card type 2', 'value'),
               Input('rating type 2', 'value'),
               Input('position type 2', 'value'),
               Input('nation type 2', 'value'),
               Input('league type 2', 'value')])
def price_filter1(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league)]
    filtered_df.reset_index(drop = True, inplace = True)
    club_type = []
    for club in filtered_df["Club"].unique():
        club_type.append({"label": str(club), "value": club})
    return club_type

@app.callback([Output('name text 2', 'children'),
               Output('card text 2', 'children'),
               Output('rating text 2', 'children'),
               Output('position text 2', 'children'),
               Output('nation text 2', 'children'),
               Output('league text 2', 'children'),
               Output('team text 2', 'children')],
              [Input('player name 2', 'value'),
               Input('card type 2', 'value'),
               Input('rating type 2', 'value'),
               Input('position type 2', 'value'),
               Input('nation type 2', 'value'),
               Input('league type 2', 'value'),
               Input('club type 2', 'value')])
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

@app.callback([Output('player predict price', 'figure'),
               Output('player predict price table', 'figure')],
              [Input('player name 2', 'value'),
               Input('card type 2', 'value'),
               Input('rating type 2', 'value'),
               Input('position type 2', 'value'),
               Input('nation type 2', 'value'),
               Input('league type 2', 'value'),
               Input('club type 2', 'value'),
               Input('Days Predicted', 'value')])
def set_card_type_options(selected_player, selected_card, selected_rating, selected_position, selected_nation, selected_league, selected_club, days_predicted):
    filtered_df = dis[(dis["Name"] == selected_player) & (dis["Card Type"] == selected_card) & (dis["Rating"] == selected_rating) & (dis["Position"] == selected_position) & (dis["Nation"] == selected_nation) & (dis["League"] == selected_league) & (dis["Club"] == selected_club)]

    data_original = linear_regression(filtered_df, days_predicted)

    data_original_2 = data_original[-days_predicted:]
    data_original_2 = data_original_2[["Date", "Prices"]]
    data_original_2["Prices"] = round(data_original_2["Prices"], 0)

    traces = []

    traces.append(go.Table(
                header=dict(values=list(data_original_2.columns),
                            fill_color='#222831',
                            line_color='white',
                            font=dict(color='white', size=13),
                            align='center'),
                cells=dict(values=[data_original_2["Date"], data_original_2["Prices"]],
                           fill_color='#4e525a',
                           line_color='white',
                           font=dict(color='white', size=11),
                           align='center')))

    for player in filtered_df:
        x_axis = data_original[:-days_predicted]["Date"]
        y_axis = round(data_original[:-days_predicted]["Prices"], 0)

        x_axis2 = data_original[-days_predicted:]["Date"]
        y_axis2 = round(data_original[-days_predicted:]["Prices"], 0)

        data = [go.Scatter(
                x = x_axis,
                y = y_axis,
                mode = 'lines+markers',
                line=dict(color='#cd00cd'),
                opacity = 0.4,
                name = "Past Values",
                marker = {"size": 6}
                ),
                go.Scatter(
                x = x_axis2,
                y = y_axis2,
                mode = 'lines+markers',
                line=dict(color='#00FF00'),
                opacity = 0.4,
                name = "Predicted Values",
                marker = {"size": 6}
                )
                ]
        return [{"data": data, "layout": go.Layout(title={'text': "Price Prediction {} Days : {} {} {} {}".format(days_predicted, selected_player, selected_card, selected_rating, selected_position),
                                                        'x':0.5,
                                                        'xanchor': 'center',
                                                        'yanchor': 'top', "font": {"color": "white", "size": 15}},
                                                    xaxis = {"title": "Date", "tickfont": {"size": 10}},
                                                    yaxis = {"title": "Price", "tickfont": {"size": 10}},
                                                    template= "plotly_dark",
                                                    paper_bgcolor='#222831',
                                                    legend=dict(orientation = "h",
                                                                yanchor="top",
                                                                xanchor="center",
                                                                x=0.5,
                                                                y = 1.10
                                                            ),
                                                    margin = {"l": 80, "r": 80, "b": 80, "t":80})
                                                    },
                {"data": traces, "layout": go.Layout(paper_bgcolor='#222831',
                                                            margin = {"l": 80, "r": 80, "b": 80, "t":80},
                                                            title={
                                                                    'text': "Price Prediction {} Days : {} {} {} {}".format(days_predicted, selected_player, selected_card, selected_rating, selected_position),
                                                                    'xanchor': 'center',
                                                                    'x':0.5,
                                                                    'yanchor': 'top',
                                                                    "font": {"color": "white", "size": 15}})}]

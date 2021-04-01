#################### Libraries ####################
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

#################### Application Server File ####################
from app import app
from app import server

#################### Python Layouts ####################
from apps import introduction, descriptive_statistics, player_search_database, market_index_analysis, player_information, ml_pricing_algorithm

#################### Layout ####################
app.layout = html.Div(children=[
	dcc.Tabs(
    	id="tabsID",
    	children=[
		dcc.Tab(label='Introduction',
				children=[introduction.layout],
                selected_style = {'backgroundColor' : "#4e525a", 'color': 'white'},
                style = {'backgroundColor' : "#222831", 'color': 'white'}),

		dcc.Tab(label='Descriptive Statistics',
				children=[descriptive_statistics.layout],
                selected_style = {'backgroundColor' : "#4e525a", 'color': 'white'},
                style = {'backgroundColor' : "#222831", 'color': 'white'}),

		dcc.Tab(label='Player Search Database',
				children=[player_search_database.layout],
                selected_style = {'backgroundColor' : "#4e525a", 'color': 'white'},
                style = {'backgroundColor' : "#222831", 'color': 'white'}),

		dcc.Tab(label='Market Index Analysis',
				children=[market_index_analysis.layout],
                selected_style = {'backgroundColor' : "#4e525a", 'color': 'white'},
                style = {'backgroundColor' : "#222831", 'color': 'white'}),

		dcc.Tab(label='Player Information',
				children=[player_information.layout],
                selected_style = {'backgroundColor' : "#4e525a", 'color': 'white'},
                style = {'backgroundColor' : "#222831", 'color': 'white'}),

		dcc.Tab(label='ML Pricing Algorithm',
				children=[ml_pricing_algorithm.layout],
                selected_style = {'backgroundColor' : "#4e525a", 'color': 'white'},
                style = {'backgroundColor' : "#222831", 'color': 'white'})
		],
    	value="Introduction"
	)
])


if __name__ == '__main__':
  app.run_server()

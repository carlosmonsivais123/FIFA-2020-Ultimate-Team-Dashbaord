#################### Libraries ####################
import dash
import dash_html_components as html
import warnings
warnings.filterwarnings("ignore")
import base64


#################### Image Path ####################
image_filename = 'assets/fifa20.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

#################### Layout ####################
layout  = html.Div([
                  html.Div(children = [html.H1("FIFA Ultimate Team 2020 Gold Players Dashboard Page"),
                                      html.H3('''Welcome to my FUT 2020 Dashboard! On this dashboard you will gain insights about the game as a whole,
                                              individual players, and the FUT 2020 market.''')],
                                      style = {'padding' : '10px' ,
                                               'backgroundColor' : '#e0e0e0',
                                               'text-align': 'center', 'width': '100%',
                                               'display': 'inline-block', 'verticalAlign': 'top', 'padding':'0px'
                                               }),

                          html.Div([
                              html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()))],
                              style={'textAlign': 'center', 'backgroundColor' : '#e0e0e0'}),

                              html.Div(children = [
                                                  html.H2('''Dashboard Created By: Carlos Monsivais''')],
                                                  style = {'padding' : '10px' ,
                                                           'backgroundColor' : '#e0e0e0',
                                                           'text-align': 'center', 'width': '100%',
                                                           'display': 'inline-block', 'verticalAlign': 'top', 'padding':'0px'
                                                           })
])

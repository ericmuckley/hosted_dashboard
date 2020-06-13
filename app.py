# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


# specify path of data file - should be in same directory as app.py
DATAPATH = 'STARRYDB_interpolated_pp_wc.csv'

# CSS stylesheet for page style - should be in same directory as app.py
STYLESHEET = 'stylesheet.css'

# title for the browser page tab
TITLE = 'STARRYDB explorer'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def get_dropdown_options(df):
    """Get the dropdown options to show for plot variables"""
    options = []
    for c_raw in list(df):
        c = c_raw.split(': ')[1] if ': ' in c_raw else c_raw
        options.append({'label': c, 'value': c_raw})
    return options

def get_labels(col):
    """Get labels to use as hover text over points, based on the
    name of the column thats being plotted"""
    return list(df['FORMULA'].iloc[np.where(df[col].notnull())[0]])

    
# import data into dataframe
df = pd.read_csv(DATAPATH)
# use this for fast testing
#df = pd.DataFrame(np.random.random((30, 4)), columns=['a','b','c','d'])

options = get_dropdown_options(df)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#import flask
#server = flask.Flask(__name__)
#server.secret_key = os.environ.get(
#    'secret_key', str(np.random.randint(0, 1000000)))


import dash
import dash_core_components as dcc
import dash_html_components as html


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# setup the server and app
app = dash.Dash(__name__, #server=server,
                external_stylesheets=[STYLESHEET]
                )
app.title = TITLE
app.css.config.serve_locally = True
server = app.server  # this line is required for web hosting


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Put your Dash page layout code here

# create app layout
app.layout = html.Div(children=[
    
    # top heading
    html.H1(children=TITLE),

    # create HTML division with paragraph for intro information
    html.Div([
        html.P([
            html.B('Dataset: '), str(DATAPATH), html.Br(),
            html.B('Total rows: '), str(df.shape[0]), html.Br(),
            html.B('Total columns: '), str(df.shape[1]), html.Br()])]),

    # division for the X dropdown menu
    html.Div([
        dcc.Dropdown(
            id='x_var_dropdown',
            options=options,
            placeholder="Select variable for X-axis (optional)",
            style=dict(width='60%', verticalAlign="middle"))]),

    # division for the Y dropdown menu
    html.Div([
        dcc.Dropdown(
            id='y_var_dropdown',
            options=options,
            placeholder="Select variable for Y-axis",
            style=dict(width='60%', verticalAlign="middle"))]),
    
    # create plot
    dcc.Graph(id='graph', config={"displaylogo": False})

])

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Here, create callbacks which are used by objects on the page

# update graph
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('x_var_dropdown', 'value'),
     dash.dependencies.Input('y_var_dropdown', 'value')])
def update_graph(X, Y):
    """Update the graph when variable selections are changed"""
    
    # take care of all edge cases in dropdown menus
    if X is None and Y is None:
        x, y = None, None
        record_num = 0
        hover_text = None

    elif X is None and Y is not None:
        y = list(df[Y].dropna())
        x = list(np.arange(len(y))+1)
        record_num = len(y)
        hover_text = get_labels(Y)
        
    elif Y is None and X is not None:
        x = list(df[X].dropna())
        y = list(np.zeros_like(x))
        record_num= len(y)
        hover_text = get_labels(X)
    
    elif X is not None and Y is not None:
        dfs = df[[X, Y]].dropna()
        x = list(dfs[X])
        y = list(dfs[Y])
        record_num= len(y)  
        hover_text = get_labels(Y)

    # error catching for axis labels
    X = 'None' if X is None else X
    Y = 'None' if Y is None else Y

    return {
        'data': [
            {'x': x,
             'y': y,
             'text': hover_text,
             'hoverinfo': 'text',
             'mode': 'markers',
             'marker': {'size': 6}}
            ],
        'layout': {'title':'Plotting {} records'.format(record_num),
                   'xaxis': {'title': X},
                   'yaxis': {'title': Y},
                   'margin': {'l': 150, 'r': 150, 'b': 150, 't': 50}}
        }


'''
# update division which reads dropdown menu
@app.callback(
    dash.dependencies.Output('x_var_display', 'children'),
    [dash.dependencies.Input('x_var_dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)
'''

             
if __name__ == '__main__':
    app.run_server(debug=True)

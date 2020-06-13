# -*- coding: utf-8 -*-

# %% Use this section to test data manipulation - doesn't need Dash


import os
import pathlib
import numpy as np
import pandas as pd


DATANAME = 'STARRYDB_interpolated_pp_wc.csv'
DATAPATH = os.path.join(
    pathlib.Path(__file__).parent.absolute(),
    'data',
    DATANAME)


# for reading data directly from Github - still some problem parsing it
#DATAPATH = 'https://github.com/ericmuckley/hosted_dashboard/
#blob/master/data/STARRYDB_interpolated_pp_wc.csv'

df = pd.read_csv(DATAPATH)[::500]
print(df.head)

x_var = 'PROPERTY: Temperature (K)'


df = pd.DataFrame(np.random.random((30, 6)),
                  columns=['a','b','c','d','e','f'])


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


def get_dropdown_options(df):
    """Get the dropdown options to show for plot variables"""
    options = []
    for c_raw in list(df):
        c = c_raw.split(': ')[1] if ': ' in c_raw else c_raw
        options.append({'label': c, 'value': c})
    return options
  



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import dash
import dash_core_components as dcc
import dash_html_components as html


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


# create app with stylesheet
external_stylesheets = ['stylesheet.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# create app layout
app.layout = html.Div(children=[
    
    # top heading
    html.H1(children='STARRYDB explorer'),


    # create HTML division with paragraph for intro information
    html.Div([
        html.P([
            html.B('Dataset: '), str(DATANAME), html.Br(),
            html.B('Total rows: '), str(df.shape[0]), html.Br(),
            html.B('Total columns: '), str(df.shape[1]), html.Br()])]),
    

    # division for the X dropdown menu
    html.Div([
        dcc.Dropdown(
            id='x_var_dropdown',
            options=get_dropdown_options(df),
            placeholder="Select variable for X-axis (optional)",
            style=dict(width='50%', verticalAlign="middle"))]),

    # division for the Y dropdown menu
    html.Div([
        dcc.Dropdown(
            id='y_var_dropdown',
            options=get_dropdown_options(df),
            placeholder="Select variable for Y-axis",
            style=dict(width='50%', verticalAlign="middle"))]),

    
    # create plot
    dcc.Graph(id='graph'),

    #html.Div(id='x_var_display'),


])

    
# update graph
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('x_var_dropdown', 'value'),
     dash.dependencies.Input('y_var_dropdown', 'value')])
def update_graph(X, Y):
    return {
        'data': [
            {'x': df[X].values,
             'y': df[Y].values,
             'name': Y}],
        'layout': {'title':'{} vs. {}'.format(Y, X)},
        'config': {'displaylogo': False}
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

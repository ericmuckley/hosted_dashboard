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
    html.H1(children='STARRYDB custom plotter'),

    
    # create HTML divisions
    html.Div(children='Dataset: {}'.format(DATANAME)),
    html.Div(children='Total rows: {}'.format(df.shape[0])),
    html.Div(children='Total rows: {}'.format(df.shape[1])),
    

    # create plot
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index,
                 'y': df[x_var].values,
                 'type': 'bar',
                 'name': x_var},
                
                #{'x': [1, 2, 3],
                # 'y': [2, 4, 5],
                # 'type': 'bar',
                # 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])




             
if __name__ == '__main__':
    app.run_server(debug=True)

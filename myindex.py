from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import dashboards, extratos, cartao_credito, investimento, sidebar


# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            html.H1("Controle Financeiro", className="text-primary"),
            # html.P("by Faslala Assis", className="text-info"),
            html.Hr(),
        ], md=4),
        dbc.Col([]),
        dbc.Col([]),
        ]), 
        
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=4),
        dbc.Col([
            
        ], md=8)
    ])

], fluid=True,)


@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extratos.layout
    
    if pathname == '/cartao_credito':
        return cartao_credito.layout
    
    if pathname == '/investimento':
        return investimento.layout


if __name__ == '__main__':
    app.run_server(debug=True)
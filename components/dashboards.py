from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
# from globals import *
from app import app

import pdb
from dash_bootstrap_templates import template_from_url, ThemeChangerAIO

card_icon= {
    "color": "white",
    "textAlign": "center",
    "fontSize": 30,
    "margin": "auto"
}

# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([

        # Saldo ---------------------------------
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Saldo"),
                    html.H5("R$ 5000", id="p-saldo-dashboards", style={}),
                ],style={"padding-left": "20px", "padding-top": "10px"}),

                dbc.Card(
                    html.Div(className="fa fa-line-chart", style=card_icon),
                    color="dark", 
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},)
            ])
        ], width=3),

        # Receita
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Receita"),
                    html.H5("R$ 3000", id="p-receita-dashboards", style={}),
                ], style={"padding-left": "20px", "padding-top": "10px"}),

                dbc.Card(
                    html.Div(className="fa fa-money", style=card_icon),
                    color="success", 
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},)
            ])
        ], width=3),

        # Despesa
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("Despesa"),
                    html.H5("R$ 2000", id="p-despesa-dashboards", style={}),
                ], style={"padding-left": "20px", "padding-top": "10px"}),

                dbc.Card(
                    html.Div(className="fa fa-spinner", style=card_icon),
                    color="info", 
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},)
            ])
        ], width=3),

        # Cartao de credito
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend("C Crédito"),
                    html.H5("R$ 800", id="p-cartao-dashboards", style={}),
                ], style={"padding-left": "20px", "padding-top": "10px"}),

                dbc.Card(
                    html.Div(className="fa fa-credit-card", style=card_icon),
                    color="warning", 
                    style={"maxWidth": 75, "height": 100, "margin-left": "-10px"},)
            ])
        ], width=3),
    ], style={'margin': '10px'}),

  
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id="graph1"), style={"padding": "10px"}), width=6),
        dbc.Col(dbc.Card(dcc.Graph(id="graph2"), style={"padding": "10px"}), width=6),
    ], style={"margin": "10px"}),

    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id="graph3"), style={"padding": "10px"}), width=6),
        dbc.Col(dbc.Card(dcc.Graph(id="graph4"), style={"padding": "10px"}), width=6),
    ], style={"margin": "10px"})   
    ])


# =========  Callbacks  =========== #


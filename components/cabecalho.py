import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from datetime import datetime, date
import pdb
from dash_bootstrap_templates import ThemeChangerAIO


layout = dbc.Row([

    dbc.Col([
        dbc.Card([
            html.H1("Controle Financeiro", className="text-primary")
            ], style={"margin-top": "3px", "margin-bottom": "3px"})
        # html.P("by Faslala Assis", className="text-info"),
    ], md=4),

    dbc.Col([], md=1),

    dbc.Col([
        dbc.Card([
            dbc.Nav([
                dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
                dbc.NavLink("Extratos", href="/extratos", active="exact"),
                dbc.NavLink("Receita", href="/receita", active="exact"),
                dbc.NavLink("Despesa", href="/despesa", active="exact"),
                dbc.NavLink("Investimento", href="/investimento", active="exact"),
                dbc.NavLink("Cartão de Crédito", href="/cartao_credito", active="exact"),
            ], pills=True, id='nav_buttons')

        ],style={"margin-top": "3px", "margin-bottom": "3px", 'padding-top': '8px', 'padding-bottom': '8px'})
          
        ], md=7)
])
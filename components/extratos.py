from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


# =========  Layout  =========== #
layout = dbc.Col([
    dbc.Row([
        html.Legend("Tabela de Despesas"),
        html.Div(id="tabela-despesas", className="dbc"),
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph', style={"margin-right": "20px"}),
        ], width=9),
        
        dbc.Col([
            dbc.Card(
                dbc.CardBody([
                    html.H4("Despesas"),
                    html.Legend("R$ 2000", id="valor_despesa_card", style={'font-size': '60px'}),
                    html.H6("Total de Despesas"),
                ], style={'text-align': 'center', 'padding-top': '30px'}))
        ], width=3),
    ]),
], style={"padding": "10px"})

# =========  Callbacks  =========== #
# Tabela

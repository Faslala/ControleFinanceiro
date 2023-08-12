import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app

from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd


# ========= Layout ========= #
layout = dbc.Col([

# Seção PERFIL
    dbc.Row([
        dbc.Col([
            dbc.Button(id='botao_avatar', children=[
                html.Img(src='/assets/man.png', id='avatar_change', alt='Avatar', className='perfil_avatar')
                ], style={'background-color': 'transparent', 'border-color': 'transparent'}),
                ], width=6),

        dbc.Col([
            html.Div([
                dbc.Button(color='success', outline=True, id='open-novo-receita', children=['+ Receita']),
                dbc.Button(color='info', outline=True, id='open-novo-despesa', children=['- Despesa']),
                dbc.Button(color='warning', outline=True, id='open-novo-cartao', children=['# Cartão de Crédito']),
                dbc.Button(color='dark', outline=True, id='open-novo-investimento', children=['* Investimento'])
                ], className="d-grid gap-2 me-1",)
                ], width=6),
                ]),
                        
        # Modal Receita
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Receita')),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Descrição: '),
                        dbc.Input(placeholder='Ex.: dividendos da bolsa, herança, ...', id='txt-receita')
                    ], width=6),
                    dbc.Col([
                        dbc.Label('Valor: '),
                        dbc.Input(placeholder='$100.00', id='valor_receita', value='')
                    ], width=6)
                ]),
                
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Data: "),
                        dcc.DatePickerSingle(id='date-receitas',
                                             min_date_allowed=date(2020,1, 1),
                                             max_date_allowed=date(2030, 12, 31),
                                             date=datetime.today(),
                                             style={'width': '100%'})
                    ], width=4),

                    dbc.Col([
                        dbc.Label('Extras'),
                        dbc.Checklist(
                            options=[],
                            value=[],
                            id='switches-input-receita',
                            switch=True
                        )                      
                    ], width=4),

                    dbc.Col([
                        html.Label('Categoria da Receita'),
                        dbc.Select(id='select_receita', options=[], value=[])

                    ], width=4)
                ], style={'margin-top': '25px'}),

                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Adicionar Categoria', style={'color': 'green'}),
                                    dbc.Input(type='text', placeholder='Nova Categoria...', id='input-add-receita', value=''),
                                    html.Br(),
                                    dbc.Button('Adicionar', class_name='btn btn-success', id='add-category-receita', style={'margin-top': '20px'}),
                                    html.Br(),
                                    html.Div(id='category-div-add-receita', style={})
                                ], width=6),
                                
                                dbc.Col([
                                    html.Legend('Excluir Categorias', style={'color': 'red'}),
                                    dbc.Checklist(
                                        id='checkist-selected-style-receita',
                                        options=[],
                                        value=[],
                                        label_style={'color': 'red'},
                                        input_checked_style={'background-color': 'blue', 'borderColor': 'orange'},
                                    ),
                                    dbc.Button('Remover', color='warning', id='remove-category-receita', style={'margin-top': '20px'}),
                                ], width=6)
                            ])
                        ])
                    ])
                ])
            ])
        ], id='modal-novo-receita'),

        # Modal Despesa
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Despesa')),
            dbc.ModalBody([])
        ], id='modal-novo-despesa'),

        # Modal Cartão de Crédito
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Compras')),
            dbc.ModalBody([])
        ], id='modal-novo-cartao'),

        # Modal Investimento
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Adicionar Investimento')),
            dbc.ModalBody([])
        ], id='modal-novo-investimento'),


        html.Hr(),
        dbc.Nav([
            dbc.NavLink("Dashboard", href="/dashboards", active="exact"),
            dbc.NavLink("Extratos", href="/extratos", active="exact"),
            dbc.NavLink("Receita", href="/receita", active="exact"),
            dbc.NavLink("Despesa", href="/despesa", active="exact"),
            dbc.NavLink("Investimento", href="/investimento", active="exact"),
            dbc.NavLink("Cartão de Crédito", href="/cartao_credito", active="exact"),
        ], vertical=True, pills=True, id='nav_buttons', style={"margin-bottons": "50px"}),

    ], id='sidebar_completa')


# =========  Callbacks  =========== #
# Pop-up receita
@app.callback(
    Output("modal-novo-receita", "is_open"),
    Input("open-novo-receita", "n_clicks"),
    State("modal-novo-receita", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# Pop-up despesa
@app.callback(
    Output("modal-novo-despesa", "is_open"),
    Input("open-novo-despesa", "n_clicks"),
    State("modal-novo-despesa", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up cartao de credito
@app.callback(
    Output("modal-novo-cartao", "is_open"),
    Input("open-novo-cartao", "n_clicks"),
    State("modal-novo-cartao", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open

# Pop-up investimento
@app.callback(
    Output("modal-novo-investimento", "is_open"),
    Input("open-novo-investimento", "n_clicks"),
    State("modal-novo-investimento", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    
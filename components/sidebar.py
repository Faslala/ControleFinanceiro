import os
import dash
import json
import plotly.express as px
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from datetime import datetime, date
from datetime import date, datetime, timedelta
import pdb
from dash_bootstrap_templates import ThemeChangerAIO

# ========= DataFrames ========= #
import numpy as np
import pandas as pd
from globals import *

# df_cat_receita = pd.read_csv("C:\\Users\\Rodrigo\\Desktop\\Dash - Rodrigo "
#                              "Vanzelotti\\MyBudget\\MyBudget\\df_cat_receita.csv")
# cat_receita = df_cat_receita['Categoria'].tolist()
#
# df_cat_despesa = pd.read_csv("C:\\Users\\Rodrigo\\Desktop\\Dash - Rodrigo "
#                              "Vanzelotti\\MyBudget\\MyBudget\\df_cat_despesa.csv")
# cat_despesa = df_cat_despesa['Categoria'].tolist()

# ========= Layout ========= #
# Seção PERFIL ------------------------
layout = dbc.Card([

    # Seção PERFIL -------------------------
    dbc.Row([
        dbc.Col([
            dbc.Button(id='botao_avatar', children=[
                html.Img(src='/assets/man.png', id='avatar_change', alt='Avatar', className='perfil_avatar')],
                       style={'background-color': 'transparent', 'border-color': 'transparent'})
        ], width=5),

        dbc.Col([
            html.Div([
                dbc.Button(color='success', outline=True, id='open-novo-receita', children=['+ Receita']),
                dbc.Button(color='info', outline=True, id='open-novo-despesa', children=['- Despesa']),
                dbc.Button(color='warning', outline=True, id='open-novo-cartao', children=['# Cartão de Crédito']),
                dbc.Button(color='dark', outline=True, id='open-novo-investimento', children=['* Investimento'])
            ], className="d-grid gap-2 me-1")
        ], width=7),

        html.Br(),
        html.Hr(),

        # Seção FILTAR LANÇAMENTOS
        dbc.Row([
            dbc.Col([
                html.Legend("Filtrar lançamentos", className="card-title"),
                html.Label("Categorias das Receitas"),
                html.Div(
                    dcc.Dropdown(id="dropdown-receita",
                                 clearable=False,
                                 style={"width": "100%"},
                                 persistence=True,
                                 persistence_type="session",
                                 multi=True),
                ),

                html.Label("Categorias das Despesas", style={'margin-top': '10px'}),
                html.Div(
                    dcc.Dropdown(id="dropdown-despesa",
                                 clearable=False,
                                 style={"width": "100%"},
                                 persistence=True,
                                 persistence_type="session",
                                 multi=True)),

                html.Label("Categorias do Cartão de Crédito", style={'margin-top': '10px'}),
                html.Div(
                    dcc.Dropdown(id="dropdown-cartao",
                                 clearable=False,
                                 style={"width": "100%"},
                                 persistence=True,
                                 persistence_type="session",
                                 multi=True)),

                html.Label("Categorias dos Investimentos", style={'margin-top': '10px'}),
                html.Div(
                    dcc.Dropdown(id="dropdown-investimento",
                                 clearable=False,
                                 style={"width": "100%"},
                                 persistence=True,
                                 persistence_type="session",
                                 multi=True)),

                html.Legend("Período de Análise", style={"margin-top": "10px"}),
                dcc.DatePickerRange(
                    month_format='Do MMM, YY',
                    end_date_placeholder_text='Data...',
                    start_date=datetime.today(),
                    end_date=datetime.today() + timedelta(days=31),
                    with_portal=True,
                    updatemode='singledate',
                    id='date-picker-config',
                    style={'z-index': '100'}
                )
            ])
        ]),

        # Modal Receita ----------------------
        html.Div([
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
                            dbc.Label('Data: '),
                            dcc.DatePickerSingle(id='date-receitas',
                                                 min_date_allowed=date(2020, 1, 1),
                                                 max_date_allowed=date(2030, 12, 31),
                                                 date=datetime.today(),
                                                 style={'width': '100%'})
                        ], width=4),

                        dbc.Col([
                            dbc.Label('Extras'),
                            dbc.Checklist(
                                options=[{"label": "Foi recebida", "value": 1},
                                         {"label": "Receita Recorrente", "value": 2}],
                                value=[1],
                                id='switches-input-receita',
                                switch=True
                            )
                        ], width=4),

                        dbc.Col([
                            html.Label('Categoria da Receita'),
                            dbc.Select(id='select_receita',
                                       options=[{'label': i, 'value': i} for i in cat_receita],
                                       value=[cat_receita[0]])
                        ], width=4),
                    ], style={'margin-top': '25px'}),

                    dbc.Row([
                        dbc.Accordion([
                            dbc.AccordionItem(children=[
                                dbc.Row([
                                    dbc.Col([
                                        html.Legend('Adicionar Categoria', style={'color': 'green'}),
                                        dbc.Input(type='text', placeholder='Nova Categoria...', id='input-add-receita',
                                                  value=''),
                                        html.Br(),
                                        dbc.Button('Adicionar', class_name='btn btn-success', id='add-category-receita',
                                                   style={'margin-top': '20px'}),
                                        html.Br(),
                                        html.Div(id='category-div-add-receita', style={})
                                    ], width=6),

                                    dbc.Col([
                                        html.Legend('Excluir Categorias', style={'color': 'red'}),
                                        dbc.Checklist(
                                            id='checkist-selected-style-receita',
                                            options=[],
                                            value=[],
                                            label_checked_style={'color': 'red'},
                                            input_checked_style={'background-color': 'blue', 'borderColor': 'orange'},
                                        ),
                                        dbc.Button('Remover', color='warning', id='remove-category-receita',
                                                   style={'margin-top': '20px'})
                                    ], width=6)
                                ]),
                            ], title="Adicionar/Remover Categorias",
                            ),
                        ], flush=True, start_collapsed=True, id='accordion-receita'),

                        html.Div(id="id_teste_receita", style={"padding-top": "20px"}),

                        dbc.ModalFooter([
                            dbc.Button("Adicionar Receita", id="salvar_receita", color="success"),
                            dbc.Popover(dbc.PopoverBody("Receita Salva"), target="salvar_receita", placement="left",
                                        trigger="click"),
                        ])
                    ], style={"margin-top": "25px"}),
                ])
            ],
                style={"background-color": "rgba(17, 140, 79, 0.05)"},
                id="modal-novo-receita",
                size="lg",
                is_open=False,
                centered=True,
                backdrop=True)

        ]),

        # Modal Despesa ----------------------
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle("Adicionar Despesa")),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Descrição: "),
                        dbc.Input(placeholder="Ex.: dividendos da bolsa, herança...", id="txt-despesa"),
                    ], width=6),
                    dbc.Col([
                        dbc.Label("Valor: "),
                        dbc.Input(placeholder="$100.00", id="valor_despesa", value="")
                    ], width=6)
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Label("Data: "),
                        dcc.DatePickerSingle(id='date-despesas',
                                             min_date_allowed=date(2020, 1, 1),
                                             max_date_allowed=date(2030, 12, 31),
                                             date=datetime.today(),
                                             style={"width": "100%"}
                                             ),
                    ], width=4),

                    dbc.Col([
                        dbc.Label("Opções Extras"),
                        dbc.Checklist(
                            options=[{"label": "Foi recebida", "value": 1},
                                     {"label": "despesa Recorrente", "value": 2}],
                            value=[1],
                            id="switches-input-despesa",
                            switch=True),
                    ], width=4),

                    dbc.Col([
                        html.Label("Categoria da despesa"),
                        dbc.Select(id='select_despesa',
                                   options=[{'label': i, 'value': i} for i in cat_despesa],
                                   value=[cat_despesa[0]])
                    ], width=4)
                ], style={"margin-top": "25px"}),

                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend("Adicionar categoria", style={'color': 'green'}),
                                    dbc.Input(type="text", placeholder="Nova categoria...", id="input-add-despesa",
                                              value=""),
                                    html.Br(),
                                    dbc.Button("Adicionar", className="btn btn-success", id="add-category-despesa",
                                               style={"margin-top": "20px"}),
                                    html.Br(),
                                    html.Div(id="category-div-add-despesa", style={}),
                                ], width=6),

                                dbc.Col([
                                    html.Legend("Excluir categorias", style={'color': 'red'}),
                                    dbc.Checklist(
                                        id="checklist-selected-style-despesa",
                                        # options=[{"label": i, "value": i} for i in cat_despesa],
                                        value=[],
                                        label_checked_style={"color": "red"},
                                        input_checked_style={"backgroundColor": "#fa7268",
                                                             "borderColor": "#ea6258"},
                                    ),
                                    dbc.Button("Remover", color="warning", id="remove-category-despesa",
                                               style={"margin-top": "20px"}),
                                ], width=6)
                            ]),
                        ], title="Adicionar/Remover Categorias",
                        ),
                    ], flush=True, start_collapsed=True, id='accordion-despesa'),

                    dbc.ModalFooter([
                        dbc.Button("Adicionar despesa", color="success", id="salvar_despesa", value="despesa"),
                        dbc.Popover(dbc.PopoverBody("Despesa Salva"), target="salvar_despesa", placement="left",
                                    trigger="click"),
                    ]
                    )
                ], style={"margin-top": "25px"}),
            ])
        ],
            style={"background-color": "rgba(17, 140, 79, 0.05)"},
            id="modal-novo-despesa",
            size="lg",
            is_open=False,
            centered=True,
            backdrop=True),
    ], id='sidebar_completa'),

])


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


# Pop-up perfis
@app.callback(
    Output("modal-perfil", "is_open"),
    Input("botao_avatar", "n_clicks"),
    State("modal-perfil", "is_open")
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# Add/Remove categoria despesa
@app.callback(
    [Output("category-div-add-despesa", "children"),
     Output("category-div-add-despesa", "style"),
     Output("select_despesa", "options"),
     Output('checklist-selected-style-despesa', 'options'),
     Output('checklist-selected-style-despesa', 'value'),
     Output('stored-cat-despesas', 'data')],

    [Input("add-category-despesa", "n_clicks"),
     Input("remove-category-despesa", 'n_clicks')],

    [State("input-add-despesa", "value"),
     State('checklist-selected-style-despesa', 'value'),
     State('stored-cat-despesas', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_despesa = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt is None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

        else:
            cat_despesa = cat_despesa + [txt] if txt not in cat_despesa else cat_despesa
            txt1 = f'A categoria {txt} foi adicionada com sucesso!'
            style1 = {'color': 'green'}

    if n2:
        if len(check_delete) > 0:
            cat_despesa = [i for i in cat_despesa if i not in check_delete]

    opt_despesa = [{"label": i, "value": i} for i in cat_despesa]
    df_cat_despesa = pd.DataFrame(cat_despesa, columns=['Categoria'])
    df_cat_despesa.to_csv("df_cat_despesa.csv")
    data_return = df_cat_despesa.to_dict()

    return [txt1, style1, opt_despesa, opt_despesa, [], data_return]


# Add/Remove categoria receita
@app.callback(
    [Output("category-div-add-receita", "children"),
     Output("category-div-add-receita", "style"),
     Output("select_receita", "options"),
     Output('checklist-selected-style-receita', 'options'),
     Output('checklist-selected-style-receita', 'value'),
     Output('stored-cat-receitas', 'data')],

    [Input("add-category-receita", "n_clicks"),
     Input("remove-category-receita", 'n_clicks')],

    [State("input-add-receita", "value"),
     State('checklist-selected-style-receita', 'value'),
     State('stored-cat-receitas', 'data')]
)
def add_category(n, n2, txt, check_delete, data):
    cat_receita = list(data["Categoria"].values())

    txt1 = []
    style1 = {}

    if n:
        if txt == "" or txt is None:
            txt1 = "O campo de texto não pode estar vazio para o registro de uma nova categoria."
            style1 = {'color': 'red'}

    if n and not (txt == "" or txt is None):
        cat_receita = cat_receita + [txt] if txt not in cat_receita else cat_receita
        txt1 = f'A categoria {txt} foi adicionada com sucesso!'
        style1 = {'color': 'green'}

    if n2:
        if not check_delete:
            pass
        else:
            cat_receita = [i for i in cat_receita if i not in check_delete]

    opt_receita = [{"label": i, "value": i} for i in cat_receita]
    df_cat_receita = pd.DataFrame(cat_receita, columns=['Categoria'])
    df_cat_receita.to_csv("df_cat_receita.csv")
    data_return = df_cat_receita.to_dict()

    return [txt1, style1, opt_receita, opt_receita, [], data_return]


# Enviar Form receita
@app.callback(
    Output('store-receitas', 'data'),

    Input("salvar_receita", "n_clicks"),

    [
        State("txt-receita", "value"),
        State("valor_receita", "value"),
        State("date-receitas", "date"),
        State("switches-input-receita", "value"),
        State("select_receita", "value"),
        State('store-receitas', 'data')
    ]
)
def salve_form_receita(n, descricao, valor, date, switches, categoria, dict_receitas):
    df_receitas = pd.DataFrame(dict_receitas)

    if n and not (valor == "" or valor is None):
        valor = round(float(valor), 2)
        date = pd.to_datetime(date).date()
        categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        df_receitas.loc[df_receitas.shape[0]] = [valor, recebido, fixo, date, categoria, descricao]
        df_receitas.to_csv("df_receitas.csv")

    data_return = df_receitas.to_dict()
    return data_return


# Enviar Form despesa
@app.callback(
    Output('store-despesas', 'data'),

    Input("salvar_despesa", "n_clicks"),

    [
        State("valor_despesa", "value"),
        State("switches-input-despesa", "value"),
        State("select_despesa", "value"),
        State("date-despesas", "date"),
        State("txt-despesa", "value"),
        State('store-despesas', 'data')
    ])
def salve_form_despesa(n, valor, switches, descricao, date, txt, dict_despesas):
    df_despesas = pd.DataFrame(dict_despesas)

    if n and not (valor == "" or valor is None):
        valor = round(valor, 2)
        date = pd.to_datetime(date).date()
        # categoria = categoria[0] if type(categoria) == list else categoria

        recebido = 1 if 1 in switches else 0
        fixo = 0 if 2 in switches else 0

        if descricao is None or descricao == "":
            descricao = 0

        df_despesas.loc[df_despesas.shape[0]] = [valor, recebido, fixo, date, descricao, txt]
        df_despesas.to_csv("df_despesas.csv")

    data_return = df_despesas.to_dict()
    return data_return

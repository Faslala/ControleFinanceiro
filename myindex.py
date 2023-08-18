from dash import html, dcc
from dash.dependencies import Input, Output
from app import *
from globals import *
from components import dashboards, extratos, cartao_credito, investimento, sidebar, cabecalho

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dcc.Store(id='store-receitas', data=df_receitas.to_dict()),
    dcc.Store(id="store-despesas", data=df_despesas.to_dict()),
    dcc.Store(id='stored-cat-receitas', data=df_cat_receita.to_dict()),
    dcc.Store(id='stored-cat-despesas', data=df_cat_despesa.to_dict()),
    dcc.Store(id='stored-cat-pagamento', data=df_cat_pagamento.to_dict()),

    dbc.Row([ 
        dcc.Location(id='url'),
        cabecalho.layout
        ]), 
        
    dbc.Row([
        dbc.Col([
            sidebar.layout
        ], md=4),
        dbc.Col([
            content
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

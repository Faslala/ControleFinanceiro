import pandas as pd
import os

if ("df_despesas.csv" in os.listdir()) and ("df_receitas.csv" in os.listdir()):
    df_despesas = pd.read_csv("df_despesas.csv", index_col=0, parse_dates=True)
    df_receitas = pd.read_csv("df_receitas.csv", index_col=0, parse_dates=True)
    df_despesas["Data"] = pd.to_datetime(df_despesas["Data"])
    df_receitas["Data"] = pd.to_datetime(df_receitas["Data"])
    df_despesas["Data"] = df_despesas["Data"].apply(lambda x: x.date())
    df_receitas["Data"] = df_receitas["Data"].apply(lambda x: x.date())

else:
    data_structure = {'Valor': [],
                      'Efetuado': [],
                      'Fixo': [],
                      'Data': [],
                      'Categoria': [],
                      'Descrição': [],
                      'Pagamento': []}

    df_receitas = pd.DataFrame(data_structure)
    df_despesas = pd.DataFrame(data_structure)
    df_despesas.to_csv("df_despesas.csv")
    df_receitas.to_csv("df_receitas.csv")

if (("df_cat_receita.csv" in os.listdir()) and ("df_cat_despesa.csv" in os.listdir()) and
        ("df_cat_pagamento.csv" in os.listdir())):
    df_cat_receita = pd.read_csv("df_cat_receita.csv", index_col=0)
    df_cat_despesa = pd.read_csv("df_cat_despesa.csv", index_col=0)
    df_cat_pagamento = pd.read_csv("df_cat_pagamento.csv", index_col=0)
    cat_receita = df_cat_receita.values.tolist()
    cat_despesa = df_cat_despesa.values.tolist()
    cat_pagamento = df_cat_pagamento.values.tolist()

else:
    cat_receita = {'Categoria': ["Salário", "Aluguel", "13o", "Férias", "Mesada", "Presente", "Reembolso Médico"]}
    cat_despesa = {
        'Categoria': ["Alimentação", "Aluguel", "Gasolina", "Saúde", "Lazer", "Condomínio", "Internet residencial"]}
    cat_pagamento = {'Pagamento': ["Pix", "Débito", "Crédito", "Dinheiro", "TED / DOC"]}

    df_cat_receita = pd.DataFrame(cat_receita, columns=['Categoria'])
    df_cat_despesa = pd.DataFrame(cat_despesa, columns=['Categoria'])
    df_cat_pagamento = pd.DataFrame(cat_pagamento, columns=['Pagamento'])
    df_cat_receita.to_csv("df_cat_receita.csv")
    df_cat_despesa.to_csv("df_cat_despesa.csv")
    df_cat_pagamento.to_csv("df_cat_pagamento.csv")

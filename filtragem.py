import pandas as pd 

dados = pd.read_excel("Vendas.xlsx")

Dados = dados[dados["ID Loja"].isin(["Shopping Morumbi"])]

dados = Dados[["ID Loja","Produto","Quantidade"]]

dados.to_excel("Vendas_Filtrada.xlsx")

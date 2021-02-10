import pandas as pd
from IPython.display import display

#Importando a base de Dados
clientes_df = pd.read_csv('ClientesBanco.csv', encoding='latin1')
clientes_df = clientes_df.drop('CLIENTNUM', axis=1)
display(clientes_df)

#Tratamentos e visão geral dos dados
clientes_df = clientes_df.dropna()
display(clientes_df.info())
display(clientes_df.describe())

# Agora vamos analisar a base, como estão divididos os clientes e os cancelados 
display(clientes_df['Categoria'].value_counts())
display(clientes_df['Categoria'].value_counts(normalize=True))

#analisando os dados
import plotly.express as px

def grafico_coluna_categoria(coluna, tabela):
  fig = px.histogram(tabela, x=coluna, color='Categoria') # color_discrete_sequence=['#e6ad12', '#02b013']
  fig.show()

for coluna in clientes_df:
  grafico_coluna_categoria(coluna, clientes_df)

#olhando mais a fundo
cancelados_df = clientes_df.loc[clientes_df['Categoria'] == 'Cancelado', :]

fig = px.histogram(cancelados_df, x='Qtde Transacoes 12m', nbins=5)
fig.show()

fig = px.histogram(cancelados_df, x="Valor Transacoes 12m", nbins=7)
fig.show()

criticos_df = cancelados_df.loc[cancelados_df['Qtde Transacoes 12m'] < 60, :]
fig = px.histogram(criticos_df, x='Contatos 12m')
fig.show()

qtde_ultra_criticos = len(criticos_df.loc[criticos_df['Contatos 12m'] > 2, :])

percentual_criticos = qtde_ultra_criticos / len(cancelados_df)
print(f'{percentual_criticos:.1%}')

#Vamos ver como os Cancelados estão divididos ao todo
for coluna in cancelados_df:
  grafico_coluna_categoria(coluna, cancelados_df)


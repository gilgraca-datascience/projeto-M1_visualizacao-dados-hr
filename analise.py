'''
Caso esteja em um ambiente virtual (venv) novo:

É necessário instalar as bibliotecas pandas, matplotlib e seaborn.
Usar o terminal do VS Code (tecla de atalho: Ctrl + `) para instalar as bibliotecas.
A biblioteca numpy já vem instalada junto com o pandas. Caso não aconteça, instale.

Opção 1: Instalação das bibliotecas: (copie o comando abaixo e cole no terminal do VS Code)
    python -m pip install pandas matplotlib seaborn
Versões utilizadas:
    pandas      3.0.6
    numpy       2.5.3
    matplotlib  3.11.2
    seaborn     0.13.2

Opção 2: rodar o arquivo requirements.txt (copie o comando abaixo e cole no terminal do VS Code)
    python -m pip install -r requirements.txt
OBS: o arquivo requirements.txt deve estar no diretório do projeto, para a instalação funcionar corretamente. 
E o arquivo está disponível no repositório do projeto (github).

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('query_1.csv')

# Análise exploratória dos dados

print(f"As 5 primeiras linhas do DataFrame:\n{df.head()}\n")
print(f"As 5 últimas linhas do DataFrame:\n{df.tail()}\n")
print("Informações sobre o DataFrame:")
df.info()
print(f"\nTamanho do DataFrame:\n{df.shape}\n")
print(f"Colunas do DataFrame:\n{df.columns.to_list()}\n")
print(f"Tipos de dados do DataFrame:\n{df.dtypes}\n")
print(f"Estatísticas descritivas para colunas numéricas:\n{df.describe(include=['number'])}\n")
print(f"Estatísticas descritivas para colunas de string e categoria:\n{df.describe(include=['str', 'category'])}\n")

# analisando inconsistências dos dados

print(f"Valores nulos por coluna:\n{df.isnull().sum()}\n")
print(f"Valores duplicados:\n{df.duplicated().sum()}\n")
print(f"Cargos únicos:\n{df['CARGO'].unique()}\n")
print(f"Quantidade de cargos únicos:\n{df['CARGO'].nunique()}\n")
print(f"Departamentos únicos:\n{df['DEPARTAMENTO'].unique()}\n")
print(f"Quantidade de departamentos únicos:\n{df['DEPARTAMENTO'].nunique()}\n")

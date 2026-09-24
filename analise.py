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

# transformação de dados

# Usei IA para auxiliar na conversão da coluna SALARIO de int para float e formatação para exibir 2 casas decimais
df["SALARIO"] = pd.to_numeric(df["SALARIO"], errors="raise").astype(float)
pd.set_option("display.float_format", "{:.2f}".format)
print(df.head())
print(df['SALARIO'].dtype)

# Usei IA para auxiliar na tradução dos cargos e departamentos para português
df["DEPARTAMENTO"] = df["DEPARTAMENTO"].replace({
    "Executive": "Executivo",
    "Administration": "Administração",
    "Finance": "Finanças",
    "Accounting": "Contabilidade",
    "Sales": "Vendas",
    "Purchasing": "Compras",
    "Shipping": "Expedição",
    "IT": "Tecnologia da Informação",
    "Marketing": "Marketing",
    "Human Resources": "Recursos Humanos",
    "Public Relations": "Relações Públicas",
})

df["CARGO"] = df["CARGO"].replace({
    "President": "Presidente",
    "Administration Vice President": "Vice-presidente Administrativo",
    "Administration Assistant": "Assistente Administrativo",
    "Finance Manager": "Gerente Financeiro",
    "Accountant": "Contador",
    "Accounting Manager": "Gerente de Contabilidade",
    "Public Accountant": "Contador Público",
    "Sales Manager": "Gerente de Vendas",
    "Sales Representative": "Representante de Vendas",
    "Purchasing Manager": "Gerente de Compras",
    "Purchasing Clerk": "Auxiliar de Compras",
    "Stock Manager": "Gerente de Estoque",
    "Stock Clerk": "Auxiliar de Estoque",
    "Shipping Clerk": "Auxiliar de Expedição",
    "Programmer": "Programador",
    "Marketing Manager": "Gerente de Marketing",
    "Marketing Representative": "Representante de Marketing",
    "Human Resources Representative": "Representante de Recursos Humanos",
    "Public Relations Representative": "Representante de Relações Públicas",
})

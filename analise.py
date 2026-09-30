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

# Configura o Pandas para mostrar todas as colunas no terminal
pd.set_option('display.max_columns', None)

df_1 = pd.read_csv('query_1.csv')

# Análise exploratória dos dados query_1.
print("\n\nAnálise exploratória de dados para a Query_1.\n")

print(f"As 5 primeiras linhas do DataFrame:\n{df_1.head()}\n")
print(f"As 5 últimas linhas do DataFrame:\n{df_1.tail()}\n")
print("Informações sobre o DataFrame:")
df_1.info()
print(f"\nTamanho do DataFrame:\n{df_1.shape}\n")
print(f"Colunas do DataFrame:\n{df_1.columns.to_list()}\n")
print(f"Tipos de dados do DataFrame:\n{df_1.dtypes}\n")
print(f"Estatísticas descritivas para colunas numéricas:\n{df_1.describe(include=['number'])}\n")
print(f"Estatísticas descritivas para colunas de string e categoria:\n{df_1.describe(include=['str', 'category'])}\n")

# Analisando inconsistências dos dados

print(f"Valores nulos por coluna:\n{df_1.isnull().sum()}\n")
print(f"Valores duplicados:\n{df_1.duplicated().sum()}\n")
print(f"Valores únicos por coluna:\n{df_1.nunique()}\n")
print(f"Cargos únicos:\n{df_1['CARGO'].unique()}\n")
print(f"Departamentos únicos:\n{df_1['DEPARTAMENTO'].unique()}\n")


# Transformação de dados

# Usei IA para auxiliar na conversão da coluna SALARIO de int para float e formatação para exibir 2 casas decimais
df_1["SALARIO"] = pd.to_numeric(df_1["SALARIO"], errors="raise").astype(float)
pd.set_option("display.float_format", "{:.2f}".format)
print(f"\nApós a mudança do tipo de salário para float:\n{df_1['SALARIO'].dtype}")

# Usei IA para auxiliar na tradução dos cargos e departamentos para português
df_1["DEPARTAMENTO"] = df_1["DEPARTAMENTO"].replace({
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

df_1["CARGO"] = df_1["CARGO"].replace({
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

# Cálculos estatísticos e gráficos Query_1.

print(F"Medidas estatísticas básicas de Salário: \n{df_1['SALARIO'].agg(['mean', 'median', 'std', 'max', 'min', 'count'])}\n")

# Média salarial por cargo. Foi usado a IA para auxiliar nos ajustes do gráfico.
media_cargo = (
    df_1.groupby('CARGO')['SALARIO']
      .mean()
      .sort_values(ascending=False)
)

print(f"Média salarial por cargo:\n{media_cargo}\n")

fig, ax = plt.subplots(figsize=(10, 6))

media_cargo.plot(
    kind='barh',
    ax=ax
)

ax.set_title('Média salarial por cargo')
ax.set_xlabel('Salário médio')
ax.set_ylabel('Cargo')

# Maior salário no topo
ax.invert_yaxis()

# Mais espaço para os nomes dos cargos
plt.subplots_adjust(left=0.30, right=0.95)

plt.show()

# Média salarial por Departamento. 
media_departamento = (
    df_1.groupby('DEPARTAMENTO')['SALARIO']
      .mean()
      .sort_values(ascending=False)
)

print(f"Média salarial por departamento:\n{media_departamento}\n")

fig, ax = plt.subplots(figsize=(10, 6))

media_departamento.plot(
    kind='barh',
    ax=ax
)

ax.set_title('Média salarial por departamento')
ax.set_xlabel('Salário médio')
ax.set_ylabel('Departamento')

# Maior salário no topo
ax.invert_yaxis()

# Mais espaço para os nomes dos cargos
plt.subplots_adjust(left=0.30, right=0.95)

plt.show()

# Soma salarial por Departamento. 
soma_departamento = (
    df_1.groupby('DEPARTAMENTO')['SALARIO']
      .sum()
      .sort_values(ascending=False)
)

print(f"Soma salarial por departamento:\n{soma_departamento}\n")

fig, ax = plt.subplots(figsize=(10, 6))

soma_departamento.plot(
    kind='barh',
    ax=ax
)

ax.set_title('Soma salarial por departamento')
ax.set_xlabel('Soma de salários')
ax.set_ylabel('Departamento')

# Maior salário no topo
ax.invert_yaxis()

# Mais espaço para os nomes dos cargos
plt.subplots_adjust(left=0.30, right=0.95)

plt.show()


# Quantidade de pagamentos por Departamento. 
qtd_departamento = (
    df_1.groupby('DEPARTAMENTO')['SALARIO']
      .count()
      .sort_values(ascending=False)
)

print(f"Quantidade de pagamentos por departamento:\n{qtd_departamento}\n")

fig, ax = plt.subplots(figsize=(10, 6))

qtd_departamento.plot(
    kind='barh',
    ax=ax
)

ax.set_title('Quantidade de pagamentos por departamento')
ax.set_xlabel('Quantidade de pagamentos')
ax.set_ylabel('Departamento')

# Maior quantidade no topo
ax.invert_yaxis()

# Mais espaço para os nomes dos cargos
plt.subplots_adjust(left=0.30, right=0.95)

plt.show()

# Análise exploratória de dados para a Query_2.

print("\n\nAnálise exploratória de dados para a Query_2.\n")

#Importação dos dados
df_2 = pd.read_csv('query_2.csv')

print(f"As 5 primeiras linhas do DataFrame:\n{df_2.head()}\n")
print(f"As 5 últimas linhas do DataFrame:\n{df_2.tail()}\n")
print("Informações sobre o DataFrame:")
df_2.info()
print(f"\nTamanho do DataFrame:\n{df_2.shape}\n")
print(f"Colunas do DataFrame:\n{df_2.columns.to_list()}\n")
print(f"Tipos de dados do DataFrame:\n{df_2.dtypes}\n")
print(f"Estatísticas descritivas para colunas numéricas:\n{df_2.describe(include=['number'])}\n")
print(f"Estatísticas descritivas para colunas de string e categoria:\n{df_2.describe(include=['str', 'category'])}\n")

# Analisando inconsistências dos dados

print(f"Valores nulos por coluna:\n{df_2.isnull().sum()}\n")
print(f"Linha com valor nulo na coluna 'ESTADO':\n{df_2[df_2['ESTADO'].isna()]}\n")
print(f"Valores duplicados:\n{df_2.duplicated().sum()}\n")
print(f"Valores únicos por coluna:\n{df_2.nunique()}\n")
print(f"Cidades únicas:\n{df_2['CIDADE'].unique()}\n")
print(f"Estados únicos:\n{df_2['ESTADO'].unique()}\n")
print(f"Países únicos:\n{df_2['PAIS'].unique()}\n")

# Transformação de dados query_2

# Alterando o nome "United Kingdom of Great Britain and Northern Ireland" para United Kingdom, para facilitar a visualização do gráfico.
df_2["PAIS"] = df_2["PAIS"].replace({
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom"
})

# Alterando o nome "United States of America" para EUA, para facilitar a visualização do gráfico.
df_2["PAIS"] = df_2["PAIS"].replace({
    "United States of America": "EUA"
})

# Alterando o valor nulo do Estado de London para "Greater London", para nao ficar nulo.
df_2["ESTADO"] = df_2["ESTADO"].replace({
    np.nan: "Greater London"
})

# Usei IA para auxiliar na tradução dos departamentos para português
df_2["DEPARTAMENTO"] = df_2["DEPARTAMENTO"].replace({
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

# Cálculos estatísticos e gráficos Query_2. Foi usado a IA para auxiliar nos ajustes dos gráficos.

# Análise de dados geográficos (Estado e Cidade) com gráficos lado a lado. 

# Define o estilo visual
sns.set_theme(style="whitegrid")

# 1. Agrupamento dos dados por Estado e Cidade.
df_geo = df_2.groupby(['PAIS', 'ESTADO', 'CIDADE']).agg(
    QTD=('FUNCIONARIO_ID', 'count'),
    SOMA_SALARIO=('SALARIO', 'sum')
).reset_index().sort_values(by='SOMA_SALARIO', ascending=False)

print(f"\nSoma e quantidade por Estado e Cidade{df_geo.head(10)}\n")

# 2. Criação da figura com 2 subplots lado a lado e usando o mesmo eixo Y para ambos os gráficos (sharey=True). 
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True) 

# Gráfico 1: Quantidade de Funcionários
sns.barplot(data=df_geo, x='QTD', y='CIDADE', ax=axes[0], palette='Blues_r', hue='CIDADE', legend=False)
axes[0].set_title('Quantidade de Funcionários por Cidade', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Nº de Funcionários')
axes[0].set_ylabel('Cidade')

# Adiciona os rótulos de valores nas barras do Gráfico 1
for container in axes[0].containers:
    axes[0].bar_label(container, fmt='%d', padding=3)

# Gráfico 2: Soma dos Salários
sns.barplot(data=df_geo, x='SOMA_SALARIO', y='CIDADE', ax=axes[1], palette='Greens_r', hue='CIDADE', legend=False)
axes[1].set_title('Massa Salarial Total por Cidade ($)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Soma dos Salários ($)')
axes[1].set_ylabel('')  # Remove rótulo duplicado no eixo Y

# Adiciona os rótulos de valores nas barras do Gráfico 2 (Formatado em Moeda)
for p in axes[1].patches:
    width = p.get_width()
    if width > 0:
        axes[1].annotate(f'$ {width:,.2f}', 
                         (width, p.get_y() + p.get_height() / 2.),
                         ha='left', va='center', xytext=(5, 0), textcoords='offset points')

plt.tight_layout()
plt.show()

# Análise de dados geográficos por Departamentos.

# Define o estilo visual limpo
sns.set_theme(style="whitegrid")

# 1. Agrupamento da Soma Salarial por Cidade e Departamento
df_salarial = df_2.groupby(['CIDADE', 'DEPARTAMENTO'])['SALARIO'].sum().reset_index()

print(f"\nSoma Salarial por Cidade e Departamento:\n{df_salarial}\n")

# 2. Criação da figura
plt.figure(figsize=(14, 8))

# Gráfico de balão
scatter = sns.scatterplot(
    data=df_salarial,
    x='CIDADE',
    y='DEPARTAMENTO',
    size='SALARIO',
    sizes=(200, 2200),  # Escala do tamanho dos balões (mínimo e máximo)
    hue='DEPARTAMENTO',
    palette='Set1',
    legend=False,       # Desativa a legenda para focar nos eixos limpos
    alpha=0.85
)

# 4. Adiciona os rótulos de valores em $ diretamente ao lado/acima de cada balão
for index, row in df_salarial.iterrows():
    plt.text(
        x=row['CIDADE'],
        y=row['DEPARTAMENTO'],
        s=f"  $ {row['SALARIO']:,.0f}", # Texto do valor em $
        va='center',
        ha='left',
        fontsize=10,
        fontweight='bold',
        color='black'
    )

# 5. Estilização e Ajuste de Títulos
plt.title('Massa Salarial Total por Cidade e Departamento', fontsize=15, fontweight='bold', pad=20)
plt.xlabel('Cidade', fontsize=12, fontweight='bold', labelpad=10)
plt.ylabel('Departamento', fontsize=12, fontweight='bold', labelpad=10)

# Rotaciona o nome das cidades para melhor leitura
plt.xticks(rotation=15, fontsize=11)
plt.yticks(fontsize=11)

# Expande as margens para os textos e bolhas não ficarem cortados nas pontas
plt.margins(x=0.2, y=0.15)

plt.tight_layout()
plt.show()

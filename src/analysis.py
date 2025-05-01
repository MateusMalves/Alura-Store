import pandas as pd
import os

def carregar_dados(diretorio):
    """
    Carrega todos os arquivos CSV de um diretório em um único DataFrame.
    """
    arquivos_csv = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith('.csv')]
    dataframes = [pd.read_csv(arquivo) for arquivo in arquivos_csv]
    return pd.concat(dataframes, ignore_index=True)

def calcular_faturamento(df):
    """
    Calcula o faturamento total por loja.
    """
    return df.groupby("Local da compra")["Preço"].sum()

def calcular_media_avaliacoes(df):
    """
    Calcula a média das avaliações por loja.
    """
    return df.groupby("Local da compra")["Avaliação da compra"].mean()

def calcular_frete_medio(df):
    """
    Calcula o custo médio de frete por loja.
    """
    return df.groupby("Local da compra")["Frete"].mean()

def produtos_mais_e_menos_vendidos(df):
    """
    Identifica os produtos mais e menos vendidos por loja.
    """
    vendas = df.groupby(["Local da compra", "Produto"]).size()
    mais_vendidos = vendas.groupby("Local da compra").idxmax()
    menos_vendidos = vendas.groupby("Local da compra").idxmin()
    return mais_vendidos, menos_vendidos

def agrupar_vendas_por_localizacao(df):
    """
    Agrupa as vendas por coordenadas geográficas (latitude e longitude).
    """
    return df.groupby(["lat", "lon"]).size().reset_index(name="Quantidade de Vendas")

def calcular_vendas_por_categoria(df):
    """
    Calcula a quantidade de produtos vendidos por categoria em cada loja.
    """
    return df.groupby(["Local da compra", "Categoria do Produto"]).size()
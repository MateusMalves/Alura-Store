import matplotlib.pyplot as plt
import folium
import numpy as np
import pandas as pd
from folium.plugins import HeatMap

def grafico_faturamento(faturamento, loja):
    """
    Gera um gráfico de barras para o faturamento total de uma loja específica,
    com uma tabela vertical posicionada ao lado do gráfico.
    """
    # Criar a figura e os subplots
    fig, (ax_grafico, ax_tabela) = plt.subplots(
        nrows=1, ncols=2, figsize=(16, 8), gridspec_kw={'width_ratios': [2, 1]}
    )

    # Gráfico de barras
    x_pos = np.arange(len(faturamento)) * 1.8
    ax_grafico.bar(x_pos, faturamento, color='skyblue', edgecolor='black', width=0.8)
    ax_grafico.set_xticks(x_pos)
    ax_grafico.set_xticklabels(faturamento.index, rotation=45)
    ax_grafico.set_title(f"Faturamento Total - {loja}", fontsize=14)
    ax_grafico.set_xlabel("Estado", fontsize=12)
    ax_grafico.set_ylabel("Faturamento (R$)", fontsize=12)

    # Tabela ao lado do gráfico
    ax_tabela.axis('tight')
    ax_tabela.axis('off')
    tabela = ax_tabela.table(
        cellText=[[estado, f"R${valor:,.2f}"] for estado, valor in zip(faturamento.index, faturamento)],
        colLabels=["Estado", "Faturamento"],
        cellLoc='center',
        loc='center'
    )
    tabela.auto_set_font_size(False)
    tabela.set_fontsize(10)
    tabela.scale(1.2, 1.2)  # Ajustar o tamanho da tabela

    # Ajustar o layout geral
    plt.tight_layout()
    plt.show()

def grafico_faturamento_por_loja(faturamento, loja):
    """
    Gera um gráfico de barras para o faturamento total de uma loja específica.
    """
    faturamento_loja = faturamento.loc[loja]
    faturamento_loja.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title(f"Faturamento Total - Loja {loja}")
    plt.xlabel("Loja")
    plt.ylabel("Faturamento (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_avaliacoes(media_avaliacoes):
    """
    Gera um gráfico de barras para a média de avaliações por loja.
    """
    media_avaliacoes.plot(kind='bar', color='orange', edgecolor='black')
    plt.title("Média de Avaliações por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Média de Avaliações")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_avaliacoes(media_avaliacoes, loja):
    """
    Gera um gráfico de barras para a média de avaliações de uma loja específica.
    """
    plt.figure(figsize=(8, 6))
    media_avaliacoes.plot(kind='bar', color='orange', edgecolor='black')
    plt.title(f"Média de Avaliações - {loja}")
    plt.xlabel("Estado")
    plt.ylabel("Média de Avaliações")
    plt.xticks(rotation=45)
    for i, valor in enumerate(media_avaliacoes):
        plt.text(i, valor + 0.05, f"{valor:.2f}", ha='center', fontsize=8)
    plt.tight_layout()
    plt.show()

def grafico_frete(frete_medio):
    """
    Gera um gráfico de barras para o custo médio de frete por loja.
    """
    frete_medio.plot(kind='bar', color='green', edgecolor='black')
    plt.title("Custo Médio de Frete por Loja")
    plt.xlabel("Loja")
    plt.ylabel("Frete Médio (R$)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_frete(frete_medio, loja):
    """
    Gera um gráfico de barras para o custo médio de frete de uma loja específica.
    """
    plt.figure(figsize=(10, 6))
    barras = frete_medio.plot(kind='bar', color='green', edgecolor='black', width=0.8)
    plt.title(f"Custo Médio de Frete - {loja}")
    plt.xlabel("Estado")
    plt.ylabel("Frete Médio (R$)")
    plt.xticks(rotation=45)

    # Adicionar os valores acima das barras
    for barra in barras.patches:
        valor = barra.get_height()
        if valor > 0:  # Apenas exibir valores positivos
            plt.text(
                barra.get_x() + barra.get_width() / 2,  # Posição horizontal (centro da barra)
                valor + 0.5,  # Posição vertical (acima da barra)
                f"R${valor:.2f}",  # Formatação do valor
                ha='center',  # Centralizado horizontalmente
                va='bottom',  # Alinhado à base
                fontsize=9,
                color='black'
            )

    plt.tight_layout()
    plt.show()

def grafico_geografico(vendas_por_localizacao):
    """
    Gera um gráfico de dispersão geográfica para mostrar a distribuição das vendas.
    """
    # Verificar se as colunas necessárias existem
    colunas_necessarias = {"lat", "lon", "Vendas"}
    if not colunas_necessarias.issubset(vendas_por_localizacao.columns):
        raise KeyError(f"O DataFrame deve conter as colunas: {colunas_necessarias}.")

    # Extrair latitude, longitude e volume de vendas
    latitude = vendas_por_localizacao['lat']
    longitude = vendas_por_localizacao['lon']
    vendas = vendas_por_localizacao['Vendas']

    # Criar o gráfico de dispersão
    plt.figure(figsize=(12, 8))
    plt.scatter(
        longitude, latitude, s=vendas / 100, c='blue', alpha=0.6, edgecolors='black'
    )

    # Configurações do gráfico
    plt.title("Distribuição Geográfica das Vendas", fontsize=14)
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def grafico_geografico_por_loja(vendas_por_localizacao):
    """
    Gera um gráfico de dispersão geográfica para mostrar a distribuição das vendas por loja.
    """
    plt.figure(figsize=(12, 8))

    # Criar o gráfico de dispersão com cores diferentes para cada loja
    for loja, dados_loja in vendas_por_localizacao.groupby("Loja"):
        tamanhos = dados_loja["Vendas"] * 10
        tamanhos[tamanhos < 50] = 50  # Tamanho mínimo
        plt.scatter(
            dados_loja["lon"], dados_loja["lat"], s=tamanhos, alpha=0.6, label=f"Loja {loja}"
        )

    # Configurações do gráfico
    plt.title("Distribuição Geográfica das Vendas por Loja", fontsize=14)
    plt.xlabel("Longitude", fontsize=12)
    plt.ylabel("Latitude", fontsize=12)
    plt.legend(title="Lojas")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def grafico_categorias(vendas_por_categoria):
    """
    Gera um gráfico de barras para as categorias mais vendidas por loja.
    """
    vendas_por_categoria.unstack().plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Vendas por Categoria em Cada Loja")
    plt.xlabel("Loja")
    plt.ylabel("Quantidade de Produtos Vendidos")
    plt.legend(title="Categoria")
    plt.tight_layout()
    plt.show()

def grafico_categorias(vendas_por_categoria, loja):
    """
    Gera um gráfico de barras empilhadas para as vendas por categoria,
    com melhorias na organização e visualização.
    """
    # Verificar se vendas_por_categoria é um DataFrame válido
    if not isinstance(vendas_por_categoria, pd.DataFrame):
        raise ValueError(f"vendas_por_categoria deve ser um DataFrame, mas é {type(vendas_por_categoria).__name__}")

    # Garantir que o DataFrame não está vazio
    if vendas_por_categoria.empty:
        raise ValueError("vendas_por_categoria está vazio. Verifique os dados de entrada.")

    # Ordenar os estados pelo total de vendas
    vendas_por_categoria["Total"] = vendas_por_categoria.sum(axis=1)
    vendas_por_categoria = vendas_por_categoria.sort_values(by="Total", ascending=False).drop(columns=["Total"])

    # Criar o gráfico
    ax = vendas_por_categoria.plot(
        kind='bar', stacked=True, figsize=(14, 8),
        colormap='tab20', edgecolor='black', width=0.8
    )

    # Ajustar título e rótulos
    plt.title(f"Vendas por Categoria - {loja}", fontsize=16)
    plt.xlabel("Estado", fontsize=12)
    plt.ylabel("Quantidade de Produtos Vendidos", fontsize=12)
    plt.xticks(rotation=45, ha='right')

    # Ajustar a legenda
    handles, labels = ax.get_legend_handles_labels()
    totais = vendas_por_categoria.sum().values
    labels = [f"{label} ({total / totais.sum() * 100:.1f}%)" for label, total in zip(labels, totais)]
    ax.legend(handles, labels, title="Categoria", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)

    # Ajustar layout
    plt.tight_layout()
    plt.show()

from folium.plugins import HeatMap
import os

def mapa_de_calor(vendas_por_localizacao):
    """
    Gera um mapa de calor para mostrar a concentração de vendas.
    """
    import folium

    # Criar o mapa centralizado na média das coordenadas
    mapa = folium.Map(
        location=[vendas_por_localizacao["lat"].mean(), vendas_por_localizacao["lon"].mean()],
        zoom_start=5
    )

    # Adicionar o Heatmap
    heat_data = vendas_por_localizacao[["lat", "lon", "Vendas"]].values.tolist()
    HeatMap(heat_data, radius=15, blur=10, max_zoom=10).add_to(mapa)

    # Garantir que a pasta 'imagens/' existe
    os.makedirs("imagens", exist_ok=True)

    # Salvar o mapa na pasta 'imagens/'
    mapa.save("imagens/mapa_vendas.html")
    print("Mapa de calor salvo como 'imagens/mapa_vendas.html'.")

    return mapa

def desempenho_por_regiao(vendas_por_localizacao):
    """
    Analisa o desempenho das lojas por região (estado).
    """
    # Agrupar por estado e loja
    desempenho = vendas_por_localizacao.groupby(["Estado", "Loja"])["Vendas"].sum().unstack(fill_value=0)

    # Exibir a tabela de desempenho
    print("\nDesempenho por Região:")
    print(desempenho)

    # Criar um gráfico de barras empilhadas
    desempenho.plot(kind="bar", stacked=True, figsize=(12, 6), colormap="tab20")
    plt.title("Desempenho das Lojas por Região", fontsize=14)
    plt.xlabel("Estado", fontsize=12)
    plt.ylabel("Total de Vendas", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
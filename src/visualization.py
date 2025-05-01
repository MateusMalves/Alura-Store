import matplotlib.pyplot as plt
import folium

def grafico_faturamento(faturamento):
    """
    Gera um gráfico de barras para o faturamento total por loja.
    """
    faturamento.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title("Faturamento Total por Loja")
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

def grafico_geografico(vendas_por_localizacao):
    """
    Gera um gráfico de dispersão para visualizar vendas por localização geográfica.
    """
    plt.scatter(vendas_por_localizacao["lon"], vendas_por_localizacao["lat"], 
                s=vendas_por_localizacao["Quantidade de Vendas"] * 10, alpha=0.5, c="blue")
    plt.title("Distribuição Geográfica das Vendas")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
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

def mapa_interativo_geografico(vendas_por_localizacao, nome_arquivo="imagens/mapa_vendas.html"):
    """
    Gera um mapa interativo com a distribuição das vendas por localização geográfica.
    Salva o resultado como um arquivo HTML.
    """
    # Ponto central (média das coordenadas)
    centro_lat = vendas_por_localizacao["lat"].mean()
    centro_lon = vendas_por_localizacao["lon"].mean()

    mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=4)

    for _, row in vendas_por_localizacao.iterrows():
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=row["Quantidade de Vendas"] * 0.3,
            color='blue',
            fill=True,
            fill_opacity=0.6,
            popup=f'{row["Quantidade de Vendas"]} vendas'
        ).add_to(mapa)

    mapa.save(nome_arquivo)
    print(f"🗺️ Mapa interativo salvo em: {nome_arquivo}")
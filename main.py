from src.analysis import (
    carregar_dados,
    calcular_faturamento,
    calcular_media_avaliacoes,
    calcular_frete_medio,
    produtos_mais_e_menos_vendidos,
    calcular_vendas_por_categoria,
    agrupar_vendas_por_localizacao,
)
from src.visualization import (
    grafico_faturamento,
    grafico_avaliacoes,
    grafico_frete,
    grafico_categorias,
    grafico_geografico,  
    mapa_de_calor,
)

def main():
    diretorio_dados = "./data"
    dados = carregar_dados(diretorio_dados)

    lojas = dados["Loja"].unique()  # Identificar as lojas pelos nomes dos arquivos

    for loja in lojas:
        print(f"\nAnalisando dados da {loja}...\n")
        dados_loja = dados[dados["Loja"] == loja]  # Filtrar os dados da loja atual

        # Faturamento total por loja
        faturamento = calcular_faturamento(dados_loja)
        print(f"Faturamento total da {loja}:")
        print(faturamento)
        grafico_faturamento(faturamento, loja)

        # Média de avaliações por loja
        media_avaliacoes = calcular_media_avaliacoes(dados_loja)
        print(f"\nMédia de avaliações da {loja}:")
        print(media_avaliacoes)
        grafico_avaliacoes(media_avaliacoes, loja)

        # Frete médio por loja
        frete_medio = calcular_frete_medio(dados_loja)
        print(f"\nCusto médio de frete da {loja}:")
        print(frete_medio)
        grafico_frete(frete_medio, loja)

        # Produtos mais e menos vendidos
        mais_vendidos, menos_vendidos = produtos_mais_e_menos_vendidos(dados_loja)
        print(f"\nProdutos mais vendidos da {loja}:")
        print(mais_vendidos)
        print(f"\nProdutos menos vendidos da {loja}:")
        print(menos_vendidos)

        # Categorias mais vendidas
        vendas_por_categoria = calcular_vendas_por_categoria(dados_loja)
        grafico_categorias(vendas_por_categoria, loja)

    # Análise geográfica (opcional, se for relevante para todas as lojas juntas)
    vendas_por_localizacao = agrupar_vendas_por_localizacao(dados)
    print("\nDistribuição geográfica das vendas:")
    print(vendas_por_localizacao)

    # Gerar o gráfico de dispersão geográfica
    grafico_geografico(vendas_por_localizacao)

    # Gerar o mapa de calor
    mapa_de_calor(vendas_por_localizacao)
    

if __name__ == "__main__":
    main()
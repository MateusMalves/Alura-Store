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
    mapa_interativo_geografico,  # Importação adicionada
)

def main():
    diretorio_dados = "./data"
    dados = carregar_dados(diretorio_dados)

    # Faturamento total por loja
    faturamento = calcular_faturamento(dados)
    print("Faturamento total por loja:")
    print(faturamento)
    grafico_faturamento(faturamento)

    # Média de avaliações por loja
    media_avaliacoes = calcular_media_avaliacoes(dados)
    print("\nMédia de avaliações por loja:")
    print(media_avaliacoes)
    grafico_avaliacoes(media_avaliacoes)

    # Frete médio por loja
    frete_medio = calcular_frete_medio(dados)
    print("\nCusto médio de frete por loja:")
    print(frete_medio)
    grafico_frete(frete_medio)

    # Produtos mais e menos vendidos
    mais_vendidos, menos_vendidos = produtos_mais_e_menos_vendidos(dados)
    print("\nProdutos mais vendidos por loja:")
    print(mais_vendidos)
    print("\nProdutos menos vendidos por loja:")
    print(menos_vendidos)

    # Análise de vendas por categoria
    vendas_por_categoria = calcular_vendas_por_categoria(dados)
    print("\nVendas por categoria em cada loja:")
    print(vendas_por_categoria)
    grafico_categorias(vendas_por_categoria)

    # Análise geográfica
    vendas_por_localizacao = agrupar_vendas_por_localizacao(dados)
    print("\nDistribuição geográfica das vendas:")
    print(vendas_por_localizacao)
    grafico_geografico(vendas_por_localizacao)
    mapa_interativo_geografico(vendas_por_localizacao)  # Chamada para o mapa interativo

if __name__ == "__main__":
    main()
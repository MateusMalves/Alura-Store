# 📊 Análise das Lojas - Alura Store

Este projeto tem como objetivo analisar os dados de vendas de quatro lojas fictícias da rede **Alura Store** e recomendar qual delas o Senhor João deve vender para abrir um novo empreendimento.

---

## 📁 Estrutura do Projeto

- `src/` – Contém os scripts de análise (`analysis.py`), visualização (`visualization.py`) e execução principal (`main.py`)
- `data/` – Arquivos CSV com os dados de cada loja
- `imagens/` – Gráficos e mapa interativo salvos
- `README.md` – Este documento

---

## 📌 Tecnologias Utilizadas

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Folium (para mapa interativo)

---

## ▶️ Como Executar

1. Clone o repositório e navegue até a pasta:

```bash
git clone https://github.com/seu-usuario/alura-store-analysis.git
cd alura-store-analysis
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Coloque os arquivos `.csv` na pasta `data/` com os nomes:

```
loja_1.csv
loja_2.csv
loja_3.csv
loja_4.csv
```

5. Execute o projeto:

```bash
python main.py
```

6. Os gráficos serão mostrados na tela e salvos na pasta `imagens/`, incluindo o mapa em `mapa_vendas.html`.

---

## 📈 Métricas Analisadas

- Faturamento total por loja
- Média de avaliações dos clientes
- Custo médio de frete
- Produtos mais e menos vendidos
- Vendas por categoria
- Distribuição geográfica das vendas

---

## ✅ Recomendação Final

### Loja recomendada para venda: **Loja 4**

**Motivos:**

- Menor faturamento (R$ 1.384.498)
- Avaliação média abaixo da média das lojas (3,996)
- Apesar do menor custo médio de frete, não se destaca em volume de vendas
- Produtos de alto valor não compensam a falta de vendas consistentes
- Desempenho geográfico disperso, sem vantagem regional

**Conclusão:**  
Vender a Loja 4 representa o menor impacto negativo e permite que o Senhor João invista em um novo negócio com base em dados concretos.

---

## ✍️ Autor

Projeto desenvolvido por [Mateus Mendonça](https://github.com/MateusMalves)

[LinkedIn](https://www.linkedin.com/in/devmateusmalves/).

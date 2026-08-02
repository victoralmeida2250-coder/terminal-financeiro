# Terminal Financeiro

Aplicação em Python para consulta e visualização de cotações financeiras usando dados da AwesomeAPI.

O projeto tem como objetivo praticar consumo de API REST, tratamento de dados com Pandas e construção de uma interface simples com Streamlit.

## Objetivo

Consultar cotações de moedas como dólar, euro e bitcoin, organizar os dados retornados pela API e apresentar as informações em uma interface interativa.

## Fluxo do projeto

1. **Coleta dos dados**  
   Requisições HTTP para a AwesomeAPI usando `requests`.

2. **Tratamento dos dados**  
   Conversão do JSON retornado pela API em DataFrames com Pandas, com seleção de colunas, conversão de tipos numéricos e tratamento de datas.

3. **Visualização**  
   Exibição das cotações e gráficos em uma aplicação Streamlit, com apoio do Plotly.

## Stack utilizada

- Python
- Requests
- Pandas
- Streamlit
- Plotly

## Como executar

Clone o repositório:

```bash
git clone https://github.com/victoralmeida2250-coder/terminal-financeiro.git
```

Acesse a pasta do projeto:

```bash
cd terminal-financeiro
```

Instale as dependências:

```bash
pip install pandas streamlit requests plotly
```

Execute a aplicação:

```bash
streamlit run arquivo_principal.py
```

## Aprendizados

- Consumo de APIs com Python;
- tratamento de dados em JSON;
- organização de dados com Pandas;
- conversão de tipos e datas;
- criação de gráficos com Plotly;
- construção de uma aplicação simples com Streamlit.

## Limitações

Este projeto tem finalidade educacional.

As cotações dependem da disponibilidade e atualização da API utilizada e não devem ser interpretadas como recomendação financeira.

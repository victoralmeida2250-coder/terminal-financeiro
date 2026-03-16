## ⚙️ Arquitetura e Fluxo de Dados (ETL/ELT)
1. **Extract (Extração):** Consumo da AwesomeAPI via biblioteca `requests`, extraindo cotações de moedas (USD, EUR, BTC) com tratamento de headers (`User-Agent`) e controle de requisições (Status Code HTTP).
2. **Transform (Transformação):** Processamento na memória utilizando `Pandas`. Os dados em formato JSON são convertidos para DataFrames, onde ocorre a filtragem de colunas de interesse técnico e a tipagem estrita de dados (conversão de strings para Float e formatação de Timestamps para DateTime).
3. **Load/Serve (Disponibilização):** Deploy de uma interface web interativa utilizando `Streamlit`. As métricas diárias são exibidas em tempo real e o histórico de 30 dias é renderizado graficamente através da biblioteca `Plotly`.

## 🛠️ Stack Tecnológica
- **Linguagem:** Python
- **Manipulação de Dados:** Pandas
- **Ingestão:** Requests (REST API)
- **Visualização:** Streamlit, Plotly Express

## 🚀 Como Executar o Projeto
1. Clone este repositório: `git clone https://github.com/victoralmeida2250-coder/terminal-financeiro.git`
2. Instale as dependências: `pip install pandas streamlit requests plotly`
3. Execute o Data App: `streamlit run arquivo_principal.py`
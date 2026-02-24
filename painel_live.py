import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# Lógica da Página
st.set_page_config(page_title="Terminal Financeiro", layout="wide")
st.title("🪙 Terminal Financeiro Ao Vivo")
st.sidebar.header("Painel de Controle")

selecao = st.sidebar.selectbox("Escolha a Moeda:", ["USD", "EUR", "BTC"])
botao = st.sidebar.button("Buscar Cotação 🚀")

link = f"https://economia.awesomeapi.com.br/last/{selecao}-BRL"

disfarce = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


link = f"https://economia.awesomeapi.com.br/last/{selecao}-BRL"
dicionario = requests.get(link, headers=disfarce).json()
df_cotacoes = pd.DataFrame.from_dict(dicionario, orient="index")

df_filtrado = df_cotacoes[["name", "high", "low", "bid"]]
df_filtrado[["high", "low", "bid"]] = df_filtrado[["high", "low", "bid"]].astype(float)

# Exibição dos Principais Indicadores
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("💰 Preço Atual", value=f"R$ {df_filtrado['bid'].iloc[0]:.2f}")
with col2:
    st.metric(f"📈 Alta ({selecao})", value=f"R$ {df_filtrado['high'].iloc[0]:.2f}")
with col3:
    st.metric(f"📉 Baixa ({selecao})", value=f"R$ {df_filtrado['low'].iloc[0]:.2f}")
st.markdown("---")

# Exibição em tabela dinâmica
st.write("Dados Brutos da API:")
st.dataframe(df_filtrado, use_container_width=True)
st.markdown("---")

# Exibição Gráfica, com um gráfico de linha!
st.subheader(f"📊 Histórico de 30 Dias ({selecao})")

link_historico = f"https://economia.awesomeapi.com.br/json/daily/{selecao}-BRL/30"
resposta_hist = requests.get(link_historico, headers=disfarce).json()

df_hist = pd.DataFrame(resposta_hist)
df_hist["bid"] = df_hist["bid"].astype(float)
df_hist["Data"] = pd.to_datetime(df_hist["timestamp"], unit='s')

fig = px.line(
    df_hist,
    x="Data",
    y="bid",
    title=f"Evolução do Preço - {selecao}/BRL",
    markers=True,
    line_shape="spline"
)

st.plotly_chart(fig, use_container_width=True)
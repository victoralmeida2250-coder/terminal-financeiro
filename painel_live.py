import streamlit as st
import pandas as pd
import requests
import plotly.express as px


# configurações da página, e configuração básica de requisição

st.set_page_config(page_title="Terminal Financeiro", layout="wide")
st.title("🪙 Terminal Financeiro Ao Vivo")
st.sidebar.header("Painel de Controle")

selecao = st.sidebar.selectbox("Escolha a Moeda:", ["USD", "EUR", "BTC"])
disfarce = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
link = f"https://economia.awesomeapi.com.br/last/{selecao}-BRL"
resposta = requests.get(link, headers=disfarce)

# tratamento de erro, muitas requisições do mesmo servidor (streamlit), devido a isso, existe um bloqueio de requisição.

if resposta.status_code == 200:
    dicionario = resposta.json()
    df_cotacoes = pd.DataFrame.from_dict(dicionario, orient="index")

    df_filtrado = df_cotacoes[["name", "high", "low", "bid"]]
    df_filtrado[["high", "low", "bid"]] = df_filtrado[["high", "low", "bid"]].astype(float)

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("💰 Preço Atual", value=f"R$ {df_filtrado['bid'].iloc[0]:.2f}")
    with col2:
        st.metric(f"📈 Alta ({selecao})", value=f"R$ {df_filtrado['high'].iloc[0]:.2f}")
    with col3:
        st.metric(f"📉 Baixa ({selecao})", value=f"R$ {df_filtrado['low'].iloc[0]:.2f}")
    st.markdown("---")

    st.subheader(f"📊 Histórico de 30 Dias ({selecao})")
    link_historico = f"https://economia.awesomeapi.com.br/json/daily/{selecao}-BRL/30"
    resposta_hist = requests.get(link_historico, headers=disfarce)

    if resposta_hist.status_code == 200:
        df_hist = pd.DataFrame(resposta_hist.json())
        df_hist["bid"] = df_hist["bid"].astype(float)
        df_hist["Data"] = pd.to_datetime(df_hist["timestamp"], unit='s')

        fig = px.line(df_hist, x="Data", y="bid", markers=True, line_shape="spline")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Não foi possível carregar o histórico de 30 dias no momento.")

else:
    st.error(f"⚠️ A API de cotações bloqueou nosso acesso no momento (Erro {resposta.status_code}).")
    st.write("Isso é comum em servidores gratuitos na nuvem. O que a API nos respondeu foi:")
    st.json(resposta.json())
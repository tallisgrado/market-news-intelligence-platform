import streamlit as st
import pandas as pd
from src.news_collector import fetch_news
from src.text_analyzer import analyze_sentiment
from src.market_rules import classify_market_impact
from src.ai_analyzer import analyze_with_ai
import plotly.express as px

st.set_page_config(
    page_title="Market News Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Market News Intelligence Dashboard")
st.write("Dashboard para coleta e análise inicial de notícias financeiras via RSS.")

df = fetch_news()
df["analysis"] = df["title"].apply(analyze_sentiment)

df["sentiment"] = df["analysis"].apply(lambda x: x[0])
df["sentiment_score"] = df["analysis"].apply(lambda x: x[1])
df["market_impact"] = df.apply(
    lambda row: classify_market_impact(row["sentiment"], row["title"]),
    axis=1
)

df["Impacto Ouro"] = df["market_impact"].apply(lambda x: x["Ouro"])
df["Impacto Bolsas"] = df["market_impact"].apply(lambda x: x["Bolsas"])
df["Impacto Dólar"] = df["market_impact"].apply(lambda x: x["Dólar"])
df["Impacto Bitcoin"] = df["market_impact"].apply(lambda x: x["Bitcoin"])
df["Confiança"] = df["market_impact"].apply(lambda x: x["Confiança"])
df["Justificativa"] = df["market_impact"].apply(lambda x: x["Justificativa"])

df = df.drop(columns=["market_impact"])

df = df.drop(columns=["analysis"])

st.sidebar.header("Filtros de Notícias")

#Fontes
sources = df["source"].unique()
selected_sources = st.sidebar.multiselect(
    "Selecione as fontes de notícias:",
    sources,
    default=sources
)

#Sentimentos
sentiments = df["sentiment"].unique()
selected_sentiments = st.sidebar.multiselect(
    "Selecione os sentimentos:",
    sentiments,
    default=sentiments
)

filtered_df = df[
    (df["source"].isin(selected_sources))
    &
    (df["sentiment"].isin(selected_sentiments))
]
positivas = len(filtered_df[filtered_df["sentiment"] == "Positivo"])
negativas = len(filtered_df[filtered_df["sentiment"] == "Negativo"])
neutras = len(filtered_df[filtered_df["sentiment"] == "Neutro"])

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Notícias Coletadas", len(filtered_df))
col2.metric("Fontes Ativas", len(selected_sources))
col3.metric("Positivas", positivas)
col4.metric("Negativas", negativas)
col5.metric("Neutras", neutras)

st.subheader("📰 Notícias Coletadas")

display_df = filtered_df.rename(
    columns={
        "source": "Fonte",
        "title": "Título",
        "sentiment": "Sentimento",
        "sentiment_score": "Score",
        "published": "Data de Publicação"
    }
)
st.dataframe(
    display_df[
        [
            "Fonte",
            "Título",
            "Sentimento",
            "Score",
            "Impacto Ouro",
            "Impacto Bolsas",
            "Impacto Dólar",
            "Impacto Bitcoin",
            "Data de Publicação",
            "Confiança",
            "Justificativa",
        ]
    ],
    width="stretch"
)

st.divider()


#Funcionalidade temporariamente desativada.
#Motivo: Em testes com hardware limitado, o tempo de resposta da IA local Ollama ficou muito alto.
#Futuro: Implementação de uma analise mais aprofundada por IA com OpenAI API.

#st.subheader("🤖 Análise Avançada com IA Local")

#selected_title = st.selectbox(
    #"Selecione uma notícia para analisar com IA:",
    #filtered_df["title"].tolist()
#)

#if st.button("Executar análise com IA Local"):
    #with st.spinner("Analisando com IA local..."):
        #ai_result = analyze_with_ai(selected_title)

    #st.text_area(
        #"Resultado da análise:",
        #ai_result,
        #height=300
    #)

st.subheader("📊 Distribuição de Sentimentos")

sentiment_counts = filtered_df["sentiment"].value_counts()

fig_sentiment = px.bar(
    sentiment_counts,
    x=sentiment_counts.index,
    y=sentiment_counts.values,
    text=sentiment_counts.values,
    color=sentiment_counts.index,
    color_discrete_map={
        "Positivo": "#2ECC71",
        "Negativo": "#E74C3C",
        "Neutro": "#95A5A6"
    },
    labels={"x": "Sentimento", "y": "Quantidade"}
)

fig_sentiment.update_layout(
    template="plotly_dark",
    showlegend=False,
    height=200,
    margin=dict(l=20, r=20, t=30, b=20)

)

st.plotly_chart(fig_sentiment, use_container_width=True)

st.divider()

st.subheader("📊 Distribuição das Fontes")

source_counts = filtered_df["source"].value_counts()

fig_sources = px.bar(
    source_counts,
    x=source_counts.index,
    y=source_counts.values,
    text=source_counts.values,
    color=source_counts.index,
    labels={"x": "Fonte", "y": "Quantidade"}
)

fig_sources.update_layout(
    template="plotly_dark",
    showlegend=False,
    height=200,
    margin=dict(l=20, r=20, t=30, b=20)
)

st.plotly_chart(fig_sources, use_container_width=True)
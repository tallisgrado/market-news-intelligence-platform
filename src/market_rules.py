MACRO_KEYWORDS = {
    "fed": ["fed", "fomc", "powell", "rate", "interest", "rate cut", "rate hike"],
    "inflation": ["inflation", "cpi", "prices", "costs"],
    "risk": ["recession", "war", "crisis", "fear", "conflict", "uncertainty"],
    "crypto": ["bitcoin", "crypto", "ethereum", "blockchain"],
    "stocks": ["stock", "stocks", "earnings", "nasdaq", "s&p", "dow"]
}


def has_keyword(text, keywords):
    return any(word in text for word in keywords)


def classify_market_impact(sentiment, title):
    text = title.lower()

    impact = {
        "Ouro": "Neutro",
        "Bolsas": "Neutro",
        "Dólar": "Neutro",
        "Bitcoin": "Neutro",
        "Confiança": "Baixa",
        "Justificativa": "Análise baseada principalmente no sentimento da manchete."
    }

    if sentiment == "Positivo":
        impact["Bolsas"] = "Positivo"
        impact["Bitcoin"] = "Positivo"

    elif sentiment == "Negativo":
        impact["Ouro"] = "Positivo"
        impact["Bolsas"] = "Negativo"
        impact["Bitcoin"] = "Negativo"

    if has_keyword(text, MACRO_KEYWORDS["fed"]):
        impact["Dólar"] = "Positivo"
        impact["Ouro"] = "Negativo"
        impact["Bolsas"] = "Negativo"
        impact["Confiança"] = "Média"
        impact["Justificativa"] = "Notícia relacionada ao Fed ou juros, com impacto relevante em dólar, ouro e bolsas."

    if has_keyword(text, MACRO_KEYWORDS["inflation"]):
        impact["Dólar"] = "Positivo"
        impact["Ouro"] = "Negativo"
        impact["Bolsas"] = "Negativo"
        impact["Confiança"] = "Média"
        impact["Justificativa"] = "Notícia relacionada à inflação, normalmente sensível para juros, dólar e ativos de risco."

    if has_keyword(text, MACRO_KEYWORDS["risk"]):
        impact["Ouro"] = "Positivo"
        impact["Bolsas"] = "Negativo"
        impact["Bitcoin"] = "Negativo"
        impact["Confiança"] = "Alta"
        impact["Justificativa"] = "Notícia ligada à aversão ao risco, favorecendo ativos defensivos como ouro."

    if has_keyword(text, MACRO_KEYWORDS["crypto"]):
        impact["Bitcoin"] = sentiment
        impact["Confiança"] = "Média"
        impact["Justificativa"] = "Notícia diretamente relacionada ao mercado cripto."

    return impact
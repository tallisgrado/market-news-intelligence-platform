from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        sentiment = "Positivo"
    elif score <= -0.05:
        sentiment = "Negativo"
    else:
        sentiment = "Neutro"

    return sentiment, score
import feedparser
import pandas as pd

RSS_FEEDS = {
    "CNBC": "https://www.cnbc.com/id/100003114/device/rss/rss.html",
    "BBC Business": "https://feeds.bbci.co.uk/news/business/rss.xml",
    "Yahoo Finance": "https://finance.yahoo.com/news/rssindex",
}


def fetch_news():
    news = []
    
    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for entry in feed.entries[:10]:
            news.append({
                "source": source,
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "summary": entry.get("summary", "")
            })

    return pd.DataFrame(news)


if __name__ == "__main__":
    df = fetch_news()
    print(df.head())
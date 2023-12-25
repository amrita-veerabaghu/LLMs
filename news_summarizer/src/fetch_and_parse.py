import requests
from newspaper import Article

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


def fetch_and_parse(article_url: str):
    session = requests.Session()

    try:
        response = session.get(article_url, headers=HEADER, timeout=10)

        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()

            title = article.title
            text = article.text
            return title, text

        else:
            print(f"Failed to fetch article at {article_url}")
            return None, None
    except Exception as e:
        print(f"Error occurred while fetching article at {article_url}: {e}")
        return None, None


if __name__ == "__main__":
    example_article = \
        "https://www.artificialintelligence-news.com/2022/01/25/meta-claims-new-ai-supercomputer-will-set-records/"
    title, text = fetch_and_parse(example_article)
    print(f"Title: {title}")
    print(f"Text: {text}")

import requests
import os
from dotenv import load_dotenv

load_dotenv()


class NewsFeed:
    """
    Create a newsletter with news articles for an email.
    """

    base_url = "https://newsapi.org/v2/everything?"
    api_key = os.environ["NEWS_API_KEY"]

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._create_url()
        articles = self._get_articles(url)

        email_body = ""
        for article in articles:
            email_body = email_body + article["title"] \
                         + "\n" + article["url"] + "\n\n"
        return email_body

    def _create_url(self):
        url = f"{self.base_url}" \
              f"q={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"sortBy=publishedAt&" \
              f"apiKey={self.api_key}"
        return url

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

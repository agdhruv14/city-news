from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

NEWS_API_KEY = '061f030fb77f4cabb7c04e8ee89f2326'
NEWS_API_URL = 'https://newsapi.org/v2/everything'


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    city = data.get('city')
    news_data = get_news_data(city)
    return jsonify(news_data)


def get_news_data(city):
    news = []

    search_terms = [
        f"{city} natural calamities",
        f"{city} crime",
        f"{city} air pollution"
    ]

    for term in search_terms:
        params = {'q': term, 'apiKey': NEWS_API_KEY, 'language': 'en', 'sortBy': 'relevancy'}
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()
        search_results = response.json()

        for result in search_results.get('articles', []):
            news.append({'title': result.get('title'), 'link': result.get('url'), 'summary': result.get('description')})

    return news


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from src import scrape_yt_explore

app = Flask(__name__)


@app.route('/')
def hello():
    return scrape_yt_explore.get_youtube_trending_api()

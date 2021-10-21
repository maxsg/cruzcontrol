from flask import Flask
from .services.twitter.twitter import get_tweets

app = Flask(__name__)

@app.route("/")
def home():
    tweets = get_tweets()
    return tweets
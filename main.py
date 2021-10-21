from flask import Flask
from .services.twitter.twitter import get_tweets

app = Flask(__name__)

@app.route("/")
def hello_world():
    tweets = get_tweets()
    return tweets
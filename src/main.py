from flask import Flask
from src.services.twitter.twitter import get_tweets

app = Flask(__name__)

@app.route("/")
def home():
    tweets = get_tweets()
    return tweets

if __name__ == "__main__":
    app.run()
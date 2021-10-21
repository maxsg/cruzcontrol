from flask import Flask
from services.twitter.twitter import get_tweets
from waitress import serve

app = Flask(__name__)

@app.route("/")
def home():
    tweets = get_tweets()
    return tweets

if __name__ == "__main__":
    #We now use this syntax to server our app. 
    serve(app, host='0.0.0.0', port=3000)
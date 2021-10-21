import requests
import json
from TwitterAPI import TwitterAPI

from .constants import (
    CONSUMER_KEY,
    CONSUMER_KEY_SECRET,
    ACCESS_KEY,
    ACCESS_TOKEN_SECRET,
    BEARER_TOKEN,
    MY_USER_ID,
    TED_CRUZ_USER_ID
)

def get_user_id(username):
    pass

def get_user_tweets(user_id=None, user_name=None):
    if user_id:
        endpoint = f'users/{user_id}/tweets'
    pass

def make_request(endpoint):
    pass

def get_client():
    api = TwitterAPI(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_KEY_SECRET,
                    access_token_key=ACCESS_KEY,
                    access_token_secret=ACCESS_TOKEN_SECRET,
                    api_version='2')

def get_tweets():

    # Init twitter client API
    api = TwitterAPI(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_KEY_SECRET,
                    access_token_key=ACCESS_KEY,
                    access_token_secret=ACCESS_TOKEN_SECRET,
                    api_version='2')

    # Construct query
    base_url = 'https://api.twitter.com'
    endpoint = f'/2/users/{TED_CRUZ_USER_ID}/tweets'
    url = base_url + endpoint

    # Perform query
    resp = requests.get(url=url, headers={'Authorization': F'Bearer {BEARER_TOKEN}'})

    # Process results
    json_data = resp.json()
    # print(json_data)
    # data = json.loads(json_data)
    print(json_data)
    print(type(json_data))
    tweets = [tweet['text'] for tweet in json_data['data']]
    results = json.dumps(tweets)

    # Return results
    return json_data

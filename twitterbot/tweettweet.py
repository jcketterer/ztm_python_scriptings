# pip install tweepy
import tweepy

# config.py : where I keep my keys as constants
import config

client = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_SECRET,
    )

tweets = client.search_recent_tweets(
    query='',
    max_results = 10
)


for tweet in tweets.data:
    print(tweet.text)
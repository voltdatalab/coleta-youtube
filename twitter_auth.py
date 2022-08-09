import tweepy
import json


def authenticate():

    with open("coleta-youtube/config.json") as jsonfile:
        tt_config = json.load(jsonfile)['twitter-api-2']

        api = tweepy.Client(consumer_key=tt_config["api_key"], consumer_secret=tt_config["api_key_secret"],
                            access_token=tt_config["access_token"], access_token_secret=tt_config["access_token_secret"], wait_on_rate_limit=True)

        return api

import tweepy
import twitter_auth
import time
from datetime import datetime


def simple_tweet(param, previous_status):
    api = twitter_auth.authenticate()
    print(previous_status)
    if (previous_status):
        status = api.create_tweet(text=param, in_reply_to_tweet_id=previous_status.data['id'])
    else:
        status = api.create_tweet(text=param)

    return status


def tweet(status, previous_status, first):
    api = twitter_auth.authenticate()
    if first:
            status = api.update_status(status=status.param.body_text + " " + get_url(status.handle, status.status_id))
    else:
        status = api.update_status(
            in_reply_to_status_id=previous_status.id, status=status.param.body_text + " " + get_url(status.handle, status.status_id))
            
    return status

def end_thread(param, previous_status):
    api = twitter_auth.authenticate()
    status = api.update_status(in_reply_to_status_id=previous_status.id, status= param.body_text)
    return status

def get_url(handle, status_id):
    return "https://twitter.com/"+handle+"/status/"+str(status_id)

def tweet_hashtags(param, hashtags):
    api = twitter_auth.authenticate()
    status = api.update_status(param.body_text.format(h=hashtags))
    return status

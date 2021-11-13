'''
The following file is meant to be used for Testing Data without the use of the Kafka Cluster. The Kafka CLuster
is primarily for a pub-sub system and in general is not required for analysis, just to maintain the Velocity of Data coming
'''


import datetime
import time
import tweepy


class twitterAuth():
    """SET UP TWITTER AUTHENTHICATION"""

    def authenthicateTwitterApp(self):
        auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
        auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        return auth


class TwitterStreamer():

    """SET UP STREAMER"""
    def __init__(self):
        self.twitterAuth = twitterAuth()
    
    def stream_tweets(self):
        '''
        Parameter Explanation
        Track = A comma-separated list of phrases which will be used to determine what Tweets will be delivered on the stream. 
        stall_warnings = Setting this parameter to the string true will cause periodic messages to be delivered if the client is in danger of being disconnected.
        languages= Language of choice = "English"
        location = This represents the bounding box of Massachusetts
        '''
        while True:
            stream = ListernerTS(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
            stream.filter(track=['Restaurants', 'Food', 'Dessert'], stall_warnings=True,languages=['en'], locations=[-73.508142,41.237964,-69.928393,42.886589])

class ListernerTS(tweepy.Stream):

    def on_data(self, raw_data):
        # On Data, send to the Kafka Producer for topic
        print(raw_data)
        return True 


if __name__ == "__main__":
    TS = TwitterStreamer()
    TS.stream_tweets()
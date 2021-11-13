from confluent_kafka import Producer, KafkaError
import json
import ccloud_lib
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
        topic_name = 'twitter_tweet'
        record_key = "twitter_tweet_data"
        producer.produce(topic_name, key=record_key, value=raw_data, on_delivery=acked)
        return True 

if __name__ == '__main__':

    # Read arguments and configurations and initialize
    args = ccloud_lib.parse_args()
    config_file = args.config_file
    topic = args.topic
    conf = ccloud_lib.read_ccloud_config(config_file)

    # Create Producer instance
    producer_conf = ccloud_lib.pop_schema_registry_params_from_config(conf)
    producer = Producer(producer_conf)

    # Create topic if needed
    ccloud_lib.create_topic(conf, topic)

    delivered_records = 0

    # Optional per-message on_delivery handler (triggered by poll() or flush())
    # when a message has been successfully delivered or
    # permanently failed delivery (after retries).
    def acked(err, msg):
        global delivered_records
        """Delivery report handler called on
        successful or failed delivery of message
        """
        if err is not None:
            print("Failed to deliver message: {}".format(err))
        else:
            delivered_records += 1
            print("Produced record to topic {} partition [{}] @ offset {}"
                  .format(msg.topic(), msg.partition(), msg.offset()))


    TS = TwitterStreamer()
    TS.stream_tweets()
    producer.poll(0)


    producer.flush()

    print("{} messages were produced to topic {}!".format(delivered_records, topic))
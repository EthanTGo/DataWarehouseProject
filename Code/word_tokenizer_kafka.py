import json
from time import sleep
import nltk
nltk.download('punkt')
from kafka import KafkaConsumer, KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8')) 

'''
For every incoming message, we will perform the appropriate filter to remove messages that do not meet our requirements
Here we are taking into input the value of the tweet
'''
def filter_tweets(tweet):
    if not tweet['retweeted'] and 'RT @' not in tweet['text']:
        return True
    return False


'''
dict_keys(['created_at', 'id', 'id_str', 'text', 'source', 'truncated', 
'in_reply_to_status_id', 'in_reply_to_status_id_str', 'in_reply_to_user_id', 
'in_reply_to_user_id_str', 'in_reply_to_screen_name', 'user', 'geo', 'coordinates', 
'place', 'contributors', 'retweeted_status', 'is_quote_status', 'quote_count', 'reply_count', 
'retweet_count', 'favorite_count', 'entities', 'favorited', 'retweeted', 'filter_level', 'lang', 'timestamp_ms'])
'''
if __name__ == '__main__':
    print('Retrieving Twitter_Stream Topic...')
    topic_name = "Twitter_Stream"
    cleaned_topic_name = 'Twitter_Stream_Cleaned'
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        auto_commit_interval_ms =  5000,
        fetch_max_bytes = 128,
        max_poll_records = 100,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

    for msg in consumer:
        sleep(5)
        if(filter_tweets(msg.value)):
            tmp = nltk.word_tokenize(msg.value['text'])
            producer.send(cleaned_topic_name,tmp)
            print('Data sent to Twitter_Stream_Cleaned')
            sleep(.5)


import json
from time import sleep
from kafka import KafkaConsumer, KafkaProducer
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import re


def cleanValue(value):
    try:
        cleaned_value = value[0]
        # Removes Punctuation
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in cleaned_value:
            if ele in punc:
                cleaned_value = cleaned_value.replace(ele, "")
                cleaned_value = cleaned_value.lower()
                cleaned_value = re.sub(' ', '_', cleaned_value)
        return(cleaned_value,value[1])
    except:
        print(f"An Error Occured")

def checkValue(cleaned_value, word_list):
    check_condition = cleaned_value[0]
    if(check_condition in word_list):
        return True
    return False


if __name__ == '__main__':
    print('Retrieving Word_count Topic...')
    topic_name = "WordCount"
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        auto_commit_interval_ms =  5000,
        fetch_max_bytes = 128,
        max_poll_records = 100,
        value_deserializer=lambda x: x
    )
    food = wn.synset('food.n.02')
    food_list = list(set([w for s in food.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]))
    food_list = [word.lower() for word in food_list]
    print(food_list)
    n = 0
    full_string = ""
    for msg in consumer:
        string = bytes.decode(msg.value)
        value = string.split(',')
        try:
            # First we clean the value
            cleaned_value = cleanValue(value)
            if(checkValue(cleaned_value, food_list)):
                print(f"Adding the row {cleaned_value}")
                full_string = full_string + str(n) + ',' + str(cleaned_value[0]) + ',' + str(cleaned_value[1])
                print(str(n) + ',' + str(cleaned_value[0]) + ',' + str(cleaned_value[1]))
                full_string = full_string + "\n"
                n = n + 1
                print(f"n is currently {n}")
                if(n == 2000):
                    break
            else:
                continue
        except:
            print(f"Error Occured, Skipping this Item")

        # Filter out words

    with open('outfile.csv','w') as f:
        f.write(full_string)


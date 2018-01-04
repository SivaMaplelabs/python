from kafka import SimpleProducer, KafkaClient
import avro.schema
import io, random
from avro.io import DatumWriter
import tweepy
import requests


# To send messages synchronously
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
 
# Kafka topic
topic = "test"

# Path to user.avsc avro schema
schema_path="user.avsc"
schema = avro.schema.parse(open(schema_path).read())
requests.packages.urllib3.disable_warnings() 
consumer_key = "oJmPMCEIYFrmkWLwtourBUczv"
consumer_secret = "NL9L3vehiA6TTmCbtMcWHiU7vXbQs7PvzqT4tjkZfR2C1YAJLP"
access_key = "948532888894554113-9b62JEMCm94Lmm3PFld2LvIAFsbPuSe"
access_secret = "0loM3sEtGgK5sSQgzEnK86YH3QIlwATVk1fXG4Kjh7GOR"

def get_tweets(username):
        global global_ids
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
        # 200 tweets to be extracted
        number_of_tweets=500
        tweets = api.user_timeline(screen_name=username, count=200)
        #pdb.set_trace()
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets if tweet.id not in global_ids] # CSV file created 
        ids = [tweet.id for tweet in tweets]
        global_ids = ids
        for tweet in tweets_for_csv:
            writer = avro.io.DatumWriter(schema)
            bytes_writer = io.BytesIO()
            encoder = avro.io.BinaryEncoder(bytes_writer)
            writer.write({"name": "TwitterUserTimeline", "tweet": tweet}, encoder)
            raw_bytes = bytes_writer.getvalue()
            producer.send_messages(topic, raw_bytes)

 
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    global_ids = []
    while True:
    	get_tweets("sboomara")
 

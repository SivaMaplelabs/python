import tweepy
import requests
import pdb

requests.packages.urllib3.disable_warnings() 
consumer_key = "oJmPMCEIYFrmkWLwtourBUczv"
consumer_secret = "NL9L3vehiA6TTmCbtMcWHiU7vXbQs7PvzqT4tjkZfR2C1YAJLP"
access_key = "948532888894554113-9b62JEMCm94Lmm3PFld2LvIAFsbPuSe"
access_secret = "0loM3sEtGgK5sSQgzEnK86YH3QIlwATVk1fXG4Kjh7GOR"

def get_tweets(username):
        global global_ids
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
        #pdb.set_trace()
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets if tweet.id not in global_ids] # CSV file created 
        ids = [tweet.id for tweet in tweets]
        global_ids = ids
        for j in tweets_for_csv:
            # Appending tweets to the empty array tmp
            tmp.append(j)
 
        # Printing the tweets
        print(tmp)
 
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    global_ids = []
    while True:
    	get_tweets("sboomara")

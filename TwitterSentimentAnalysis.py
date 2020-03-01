import tweepy 
from textblob import TextBlob
import csv

consumer_key = '5OyelwrI4vJ5swWijMSE44wmJ'
consumer_secret = 'JS1oIcUdDnOoaVL2gjzgjKhFwrhIBkY5FNIbyP7cu8RAmAt016'
access_token = '4740190268-DSjDVKwg1R1yWyrFOMYLpugjnK56NibFrtC2nUi'
access_secret = 'xhg3R6EWHPXQCy51qicHPzSKkLhOyxzd3NuqVLfM0gN5B'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
public_tweets = api.search('Coronavirus')

fp = open("coronavirus.csv", "w")
writer = csv.writer(fp)

for tweet in public_tweets:
    info = []
    info.append(tweet.text)
    analysis = TextBlob(tweet.text)
    info.append(analysis.sentiment.polarity)
    writer.writerow(info)

fp.close()
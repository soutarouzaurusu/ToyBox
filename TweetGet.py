import tweepy
import sys
import csv

access_key = "3156467816-D0dfwQ5E0YOgnZXyNfZJkZP9a2Fd4dSULHuWG8u"
access_secret = "4hv9zdKuhT2Jh5GAPANhavAOEClJGBR3QoEIDC1XPANoe"
consumer_key = "GqbszmCS4Zc2fs7OU57zNH4ib"
consumer_secret = "9NoWdQy5u7DhesRqwviHyybV27aA8OmBvkkEG0UfFhw9TeYei8"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

user_name ="@" + sys.argv[1]
tweet_data = []

for tweet in tweepy.Cursor(api.user_timeline,screen_name = user_name,exclude_replies = True).items():
    tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

with open('tweets_' +user_name+ '.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])
    writer.writerows(tweet_data)
    pass

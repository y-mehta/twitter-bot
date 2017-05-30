# Author : Yash Mehta <https://github.com/y-mehta/twitter-bot>
# Import Tweepy
import tweepy
# Import config file
from config import *
# Import sleep
from time import sleep

# Authorizes twitter app using credentials from config file
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Iterates for loop to search and retrive tweets
# Replace q='#infosec' to your desired hashtag
# For ex; q='#example'
for tweet in tweepy.Cursor(api.search, q='#infosec').items():
    try:
	print('Tweet by: @' + tweet.user.screen_name) # Prints Username who tweeted on Terminal        
        tweet.retweet()
        print('Retweeted')
	sleep(5) # Sleep Time, Should be >5 to avoid blocking
        

    except tweepy.TweepError as error:
        print(error.reason)

    except StopIteration:
        break


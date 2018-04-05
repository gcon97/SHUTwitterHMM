from twitter import *
import time
import random

consumer_key = "E0e9MWowyQQYwB0Vev7zPeoaH"
consumer_secret = "PripaWMCSOEx1ccv1Pcsn0igUcHaXQO0DHRTFOYYokid9ZVOIF"
access_token = "980093709294493701-bj2DkX4pYCLPArfi5Devtn5kJ9e2qv0"
access_token_secret = "v0ifc1JVoPvLwB3KcK4kWMHl0vVZUFEVOAtUc53ZX70cp"


t = Twitter(auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))
tweets = []

def readdata():
    pullData = open('hmmtweets.txt','rb')
    for p in pullData:
      text = p.decode('utf-8')
      tweets.append(text)
    pullData.close()

def run():
    readdata()
    leng = len(tweets)
    for x in range(0,leng):
        sleeptime = random.randint(3600, 10400)
        tweet = tweets[x]
        print(tweet)
        t.statuses.update(status=tweet)
        print(sleeptime)
        time.sleep(sleeptime)

run()
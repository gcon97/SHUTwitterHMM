import json
import re
import nltk
from nltk.tokenize import word_tokenize
from twitter import *
import oauth2 as oauth
import time
consumer_key = "UHo0xJsh2iwYigjp92z3ABnR5"
consumer_secret = "DSmCo5XnjGtXeJ2TIZEMhbiB4rrzrBxB52W46hvsrQ7LQPf2b1"
access_token = "1297956746-MZ6cMIg4QD0lAQTDZgCj1KPuYdOSGD67DrTTypB"
access_token_secret = "2y3c1RbC7ecauOtgQ7zfHgdClaP6YFHd270DsGVpNSenQ"

consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)
access = oauth.Token(key=access_token, secret= access_token_secret)
client = oauth.Client(consumer,access)

def main():
    counter = 0
    tweetarray = []
    id_array = []
    user = input("Please input the username of the tweets you would like to collect")
    timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+user+"&count=3200&include_rts=fasle&exclude_replies=true"


    for x in range(0,17):
        response, data = client.request(timeline_endpoint)
        tweets = json.loads(data)
        for tweet in tweets:
            usertweet = (tweet["text"])
            usertweet = usertweet + ' '
            usertweet = re.sub(r'https(.*?)\s', '', usertweet)
            usertweet = re.sub(r'…', '', usertweet)
            usertweet = re.sub(r'http(.*?)\s', '', usertweet)
            tweetarray.append(usertweet)
        old = (tweet["id_str"])
        id_array.append(old)
        timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+user+"&count=3200&include_rts=fasle&exclude_replies=true&max_id="+(old)


    f = open('tweets.txt', 'a', encoding='utf-8')
    for x in tweetarray:
        counter += 1
        f.write(x + ' ' + '\n')
    print(counter)

    f.close()

main()

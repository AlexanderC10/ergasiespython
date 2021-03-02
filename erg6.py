import tweepy
import webbrowser
import time
import pandas as pd

consumer_key = "zSZKNwDgmhjW5BvnBJuTKUUhj"
consumer_secret = "OJooqiGxYnnbSm0KCubkXPSQb4Xp8pDmOCKBHe9LdwTb1Lt1Bk"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token('3883692863-7w9TfkpVoJqgBWD2mCbA4g9UHbg78oPlHNbpwu7', '1uJ9AD1DebevePcYjBBiPir8wxyXnlK6WK3JsIseDkNdj')


api = tweepy.API(auth)

handle = input("Enter the user's handle: @") # Input user 

user = api.get_user(handle)
user_timeline = user.timeline()
all_words = []
if len(user_timeline) < 10: # Check for enough tweets
    print("This user has less than 10 tweets")
    exit()
for i in range(10):
    txt = user_timeline[i].text
    txt = txt.replace('\n', ' ')
    words = txt.strip().split(' ')
    for word in words:
        if word.lower() not in all_words:
            all_words.append(word.lower())

all_words.remove('') # Remove blank entries
for i in all_words: # Remove links
    if "https://" in i or 'http://' in i:
        all_words.remove(i)

sorted_words = sorted(all_words, key=len)
print("5 smallest words:")
print(sorted_words[:5])
    
print("5 largest words:")
print(sorted_words[len(sorted_words) - 5:])


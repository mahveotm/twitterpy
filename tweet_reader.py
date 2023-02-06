import os
import time

import tweepy
from dotenv import load_dotenv

# Load the environment variables from a .env file
load_dotenv()

# Get the environment variables
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_KEY = os.getenv("ACCESS_KEY")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"


def retrieve_last_seen_id(file_name):
    with open(file_name, "r") as f_read:
        last_seen_id = int(f_read.read().strip())
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    with open(file_name, "w") as f_write:
        f_write.write(str(last_seen_id))
    return


def readtweet():
    print("retrieving tweets...")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    home = api.home_timeline(last_seen_id)
    for status in reversed(home):
        print(f"{status.id}: {status.text}")
        last_seen_id = status.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        print("found tweets")


while True:
    readtweet()
    time.sleep(45)

import tweepy
import time
# this bot just enables you to read status on the python console, does not do anything other than read.

CONSUMER_KEY = 'consumer_key'
CONSUMER_SECRET = 'consumer_secret'
ACCESS_KEY = 'access_key'
ACCESS_SECRET = 'access_secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'


"""You need to create an empty text file and name it "last_seen_id.txt" This script will read the tweet id and keep updating it when done to avoid repeating a tweet"""


def retrieve_last_seen_id(file_name):
    # File read now more secure and auto closes + fewer lines
    with open(file_name, 'r') as f_read:
        last_seen_id = int(f_read.read().strip())
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    with open(file_name, 'w') as f_write:
        f_write.write(str(last_seen_id))
    return


def readtweet():
    print('retrieving tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    home = api.home_timeline(
        last_seen_id,)
    for status in reversed(home):
        print(str(status.id)+status.text)
        # this enables you to get the status and also the status id for further use if needed
        last_seen_id = status.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        print('found tweets')


while True:
    readtweet()
    time.sleep(45)

# the time can be changed to whatever you want.
# I usd 45 sec to allow for breaks and to avoid me from exceeding the rate limit.
# Thanks,
# (c) Mahveotm, but freely usable and distributable, cheers!

import tweepy, time
# this bot just enables you to read status on the python console, does not do anything other than read.

CONSUMER_KEY ='your consumer key goes here'
CONSUMER_SECRET ='your consumer secret goes here'
ACCESS_KEY ='your access key goes here'
ACCESS_SECRET = 'your access secret goes here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'
#You need to create an empty text file and name last_seen_id.txt This script will read the tweet id and keep updating it when done to avoid repeating a tweet
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def readtweet():
    print('retrieving tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    home = api.home_timeline(
                        last_seen_id,)
    for status in reversed(home):
        print(str(status.id)+status.text)
		#this enables you to get the status and also the status id for further use if needed
        last_seen_id = status.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        print('found tweets')


while True:
    readtweet()
    time.sleep(45)
	#the time can be changed to whatever you want. I usd 45 sec to allow for breaks and to avoid me from exceeding the rate limit.
	#Thanks,
	#Mahveotm, but freely usable and distributable, cheers!

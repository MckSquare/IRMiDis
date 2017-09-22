import re
import tweet_preprocess

def process(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet
#end

#Read the tweets one by one and process it
fp = open('data/stage1.txt', 'r')
file = open('data/stage2.txt', 'w')
line = fp.readline()

while line:
    processedTweet = process(line)
    #print (processedTweet)
    file.write("%s\n" % processedTweet)
    line = fp.readline()
#end loop
fp.close()
file.close()
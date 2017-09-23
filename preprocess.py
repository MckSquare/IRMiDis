import json
import codecs, string

class Tweet_dataset:
        
        def __init__(self):
                print self
        
        #Read tweets from JSON file
        def json_parser(self, json_file):
                tweets = []
                for line in open(json_file, 'r'):
                        tweets.append(json.loads(line))
                no_of_tweets = len(tweets)             
                return tweets
                
        #Print entire tweet text data
        def print_tweet_data(self, tweets):
                no_of_tweets = len(tweets)
                for i in range(0, no_of_tweets):                        
                        data = tweets[i]
                        print data['id']
                        print data['text']
                        
                                                
        #Detect Hindi characters in the tweet data        
        def detect_language(self, character):
                maxchar = max(character)
                if u'\u0900' <= maxchar <= u'\u097f':
                        return 'hindi'
                else: 
                        return 'not'
        
                                
        #Remove non-English tweets
        def filter_tweets(self, tweets):
                filtered_tweets= []
                no_of_tweets = len(tweets)
                for i in range(0, no_of_tweets):                        
                        data = tweets[i]
                        tweet_text = data['text']
                        flag = 0
                        for word in tweet_text:
                                if self.detect_language(word)=='hindi':
                                        #print 'Removing tweet '+ str(i)
                                        flag += 1
                                        break                        
                        if flag==0:
                                #print 'Appending tweet '+ str(i)
                                filtered_tweets.append(tweets[i])                
                return filtered_tweets

                
        #Read tweet_ids from file 
        def read_id(self, file_path):
                array = []
                with open(file_path, "r") as inpfile:

                        for line in inpfile:
                                line = line.strip()
                                array.append(line)
                return array
                
                                
        #Classify tweet data in an array of 0,1,2
        def generate_output(self, tweets, tweet_id_need, tweet_id_avail):
                no_of_tweets = len(tweets)                
                Y= []
                need = 0
                avail = 0
                for i in range(0, no_of_tweets):
                        data = tweets[i]
                        tweet_text = data['text']
                        tweet_id = str(data['id'])
                        
                        if tweet_id in tweet_id_need:
                                Y.append(1)
                                #tweet_text.append(" #need")
                                need += 1
                        elif tweet_id in tweet_id_avail:
                                Y.append(2)
                                #tweet_text.append(" #availability")
                                avail += 1
                        else:
                                Y.append(0)
                print 'need: '+ str(need)
                print 'availability: '+str(avail)
                print 'total: '+ str(no_of_tweets)
                return Y

        def preprocess_text(self, tweets, tweet_id_need, tweet_id_avail):
                no_of_tweets = len(tweets)
                opfile = open("tweet_set.txt", "w")
                for i in range(0, no_of_tweets):
                        data = tweets[i]
                        tweet_text = data['text']
                        tweet_id = str(data['id'])
                        
                        if tweet_id in tweet_id_need:
                                opfile.write(u' '.join(("%s\n", tweet_text, " #need ")).encode('utf-8').strip())
                                #tweet_text.append(" #need")
                        elif tweet_id in tweet_id_avail:
                                opfile.write(u' '.join(("%s\n", tweet_text, " #availability ")).encode('utf-8').strip())
                                #tweet_text.append(" #availability")
                        else:
                                opfile.write(u' '.join((tweet_text)).encode('utf-8').strip())
               
                opfile.close()
                
                
                
                                

mObj = Tweet_dataset()

#read IDs of need and available tweets
need_tweet_IDs = mObj.read_id('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/development-set-directory/NepalQuake-need-tweetids-development-set.txt')
avail_tweet_IDs = mObj.read_id('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/development-set-directory/NepalQuake-availability-tweetids-development-set.txt')

tweet_array = mObj.json_parser('/home/pratyusha/Documents/DeepLearning/Fire2017-IRMiDis-data/microblogs-crawl-directory/NepalQuake-code-mixed-training-tweets.jsonl')
#return filtered tweets:
tweets=mObj.filter_tweets(tweet_array)

Y = mObj.generate_output(tweets, need_tweet_IDs, avail_tweet_IDs)
#print Y   
mObj.preprocess_text(tweets, need_tweet_IDs, avail_tweet_IDs)

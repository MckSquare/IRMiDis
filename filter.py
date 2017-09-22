import re

#initialize stopWords
stopWords = []

#start replaceTwoOrMore
def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

#start getStopWordList
def getStopWordList(stopWordFile):
    #read the stopwords file and build a list
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordFile, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords

#start getfeatureVector
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.')
        #check if the word stats with a hashtag
        val = re.search(r"^[#][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stopWords or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector
#end

#Read the tweets one by one and process it
fp = open('data/stage2.txt', 'r')
line = fp.readline()

st = open('data/stop.txt', 'r')
fVec=open('data/featureVector.txt', 'w')
stopWords = getStopWordList('data/stop.txt')

while line:
    #processedTweet = processTweet(line)
    featureVector = getFeatureVector(line)
    #print featureVector
    fVec.write("%s\n" %featureVector)
    line = fp.readline()
#end loop
fp.close()
st.close()
fVec.close()
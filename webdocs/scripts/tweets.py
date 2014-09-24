#!/usr/bin/python
import json
import requests
import datetime
import os, os.path

def fetchTweets():
    with file('../../twitterAccessToken','r') as f:
        accessToken = f.read() 

    tweets = json.loads(requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=scubbo&count=10', headers={'Authorization':'Bearer ' + accessToken}).text)
    for tweet in tweets:
        timestamp = timestampFromTweet(tweet)
        tweet['timestamp'] = timestamp
        cacheFilename = '../tweetCache/'+str(timestamp)
        if not os.path.exists(cacheFilename):
            with file(cacheFilename,'w') as f:
                f.write(json.dumps(tweet))

    cacheFiles = os.listdir('../tweetCache')
    cacheFiles.sort(reverse=True)
    for cacheFile in cacheFiles[:-10]:
        os.remove('../tweetCache/'+cacheFile)

    tweets = map(lambda tweet: dict(tweet.items() + [('timestamp',timestampFromTweet(tweet))]), tweets)
    return tweets

def timestampFromTweet(tweet):
    return int(datetime.datetime.strptime(' '.join(filter(lambda x: x[0]!='+' or len(x) != 5, tweet[u'created_at'].split(' '))), '%a %b %d %H:%M:%S %Y').strftime('%s'))


    

def main():
    print "Content-type: application/json"
    print
    print json.dumps(fetchTweets())

if __name__=='__main__':
    main()

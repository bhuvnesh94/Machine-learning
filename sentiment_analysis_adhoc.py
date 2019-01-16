#importing tweepy to use twitter api
import tweepy

#entering twitter developer app credentials
consumer_key= "44wLNFtgKs2R0DFnYvtXU2eoa"
consumer_secret= "5ZIkMJYWzgckhG5JFgPb8mqqj3Y0qyQbKsizsYBlWvXRnsvh6b"
access_key= "1085506066820091906-DBSRWbTbPhG78JrhaLKVPnDnPtGPmP"
access_secret= "B7euPLR6kKcMk8aosYirhDlgi3gXFVoKxTY6Kuw99t5LH"

def get_tweets(username) :
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    
    api = tweepy.API(auth)
    tweets= api.search(q=username, count=100)
    #number_of_tweets = 100
    
    #tweets = api.user_timeline(screen_name=username, #count=number_of_tweets)
    
    tmp = []
    
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        tmp.append(j)
        
    print(tmp)
    print(len(tmp))

if __name__ == '__main__':
    topic=input("enter the topic to be searched:") 
    get_tweets(topic)
    

    
    
import tweepy
import textblob as textblob

consumer_key= 'Mk2v7xvPj5BHxbbCaJGAm0d50'
consumer_secret='kxw3dEBxcHD2lam4k51VaQqxk0vCVA82BUiZ1WWrCAxcrXHuX7'

access_token='1256666371582296064-h2YoofRtfxAZjCOIWKoJuMVH5Ryj8B'
acess_token_secret='avnh44Wb7yYD5MNWBMMspY6yrwZFN40ki1ALUj94RWm8I'

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token( access_token, acess_token_secret)

api=tweepy.API(auth)

public_tweets= api.search_tweets('Lebron')

for tweets in public_tweets:
       print(tweets.text)
       analysis=TextBlob(tweet.text)
       print(analysis.sentiment)
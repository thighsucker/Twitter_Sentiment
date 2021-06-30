
from textblob import TextBlob
import csv
import tweepy

API_key = '2CnlVkOhPQQetAVbE4bEwB9xP'
API_secret = 'yMazIp8dlCHkPyqnSZs1kevzXyartsJpQ5zzVzMeMCnKmBge60'

access_token = '1409308711269531651-D6OEE03ZHJ3gKbkd7BGwkARDITJI6Z'
access_token_secret = 'WKFq9GxU0KOu5a8OVK5qERSC4Nq6sK3bZjln0attRMatT'

# authenticate with twitter

auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# retrieve steps
public_tweets = api.search('Trump')

tweet_count = 0
with open('tweets.csv', 'w', newline='\n') as f:

    writer = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment'])
    writer.writeheader()

    for tweet in public_tweets:

        # perform sentiment analysis on tweets
        text = tweet.text

        # cleaning tweet

        cleantext = ' '.join([word for word in text.split('  ') if len(word) > 0 and word[0] != '@'
        and word[0] =='.' and word[0] != '#' and 'http' not in word and word != 'RT'])

        analysis = TextBlob(tweet.text)
        sentiment = analysis.sentiment.polarity

        if sentiment >= 0:
            polarity = 'Positive'
        else:
            polarity = 'Negative'

        # print(cleantext, polarity)
        writer.writerow({'Tweet':text, 'Sentiment':polarity})

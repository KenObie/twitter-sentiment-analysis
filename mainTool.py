from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumer_key = "YOUR KEY HERE"
consumer_secret = "YOUR KEY HERE"
access_token = "YOUR KEY HERE"
access_token_secret = "YOUR KEY HERE"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

searchItem = input("Enter hashtag to analyze: | ")
noOfSearchTerms = int(input("How many tweets would you like to analyze? |"))

tweets = tweepy.Cursor(api.search, q=searchItem).items(noOfSearchTerms)
positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    #print(tweets.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    elif (analysis.sentiment.polarity < 0.00):
        negative += 1
    elif (analysis.sentiment.polarity > 0.00):
        positive += 1

positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)

positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

print("How people are reacting on " + "#" + searchItem + " by analyzing " + str(noOfSearchTerms) + " Tweets.")

if (polarity == 0):
    print("Neutral")
elif(polarity < 0):
    print("Negative")
elif(polarity > 0):
    print("Positive")

labels = ['Positive ['+str(positive)+'%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['blue', 'gold', 'red']
patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("How people are reacting to " + "#"+searchItem + " on twitter!")
plt.axis('equal')
plt.tight_layout()
plt.show()

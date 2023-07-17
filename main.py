import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


def showDataForProducts(list):
    for i in list:
        getTweets(i)


def getTweets(product):
    tweetData = []

    for i, tweet in enumerate(
            sntwitter.TwitterSearchScraper(f'bought {product} since:2022-07-16 until:2023-07-16').get_items()):
        if i > 250:
            break
        tweetData.append([tweet.content])

    return tweetData


def analyzeSentiment(data):
    analyzer = SentimentIntensityAnalyzer()
    scores = []
    for tweet in data:
        scores.append(analyzer.polarity_scores(tweet)["compound"])
    return scores


if __name__ == '__main__':
    a = analyzeSentiment(getTweets("fitbit"))
    b = analyzeSentiment(getTweets("apple watch"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

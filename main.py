import snscrape.modules.twitter as sntwitter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


def showDataForProducts(list):
    tweetDataList = []
    for i in list:
        tweetDataList.append(analyzeSentiment(getTweets(i)))
    tweetDataFrame = pd.DataFrame(data=tweetDataList, columns="Polarity Scores:")

    print(tweetDataFrame.mean())
    return


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
    showDataForProducts(["fitbit", "apple watch"])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

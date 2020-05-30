from twitter_scraper import get_tweets
for t in  get_tweets('jairbolsonaro'):
    print (t['text'], t['likes'], t['retweets'])

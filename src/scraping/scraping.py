from snscrape.modules.twitter import TwitterProfileScraper
import pandas as pd

def get_tweets(scraper, num):
    tweets_list = []
    
    for i, tweet in enumerate(scraper.get_items()):
        if i == num:
            return tweets_list
        tweets_list.append([tweet.user.displayname, tweet.renderedContent])
        
    return tweets_list

num = 100
usernames = ['EstadaoPolitica', 'CHOQUEI', 'folha', 'CNNBrasil']
tweets = []

for name in usernames:
    scraper = TwitterProfileScraper(name)
    cur_list = get_tweets(scraper, num)
    tweets += cur_list

tt_df = pd.DataFrame(tweets)
tt_df.to_csv('tweets.csv')
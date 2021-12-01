import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df_tweets=pd.read_csv('bitcoin_tweets.csv',
    dtype={
        "user_name": object,
        "user_location": object,
        "user_description": object,
        "user_created": object,
        "user_followers": float,
        "user_friends": object,
        "user_favourites": object,
        "user_verified": object,
        "date": "string",
        "text": object,
        "hashtags": object,
        "source": object,
        "is_retweet": object
    })

# PROCESS TWEETS

# drop unwanted columns
df_tweets = df_tweets.drop(columns=['user_name', 'user_location', 'user_description', 'user_created', 'user_friends',
   'hashtags', 'source',  'is_retweet'])

# find and drop strange data in date
df_tweets.drop(df_tweets[(df_tweets['date'].str.len() < 19) | (df_tweets['date'].str.len() > 19)].index, inplace = True)

#print(df_tweets['date'][(df_tweets['date'].str.len() < 19) | (df_tweets['date'].str.len() > 19)])
#print(df_tweets.iloc[693194,8])

# replace the all seconds into '00, to match with bitcoin price data
df_tweets['date'] = (df_tweets['date']).str[:-2]
df_tweets['date'] = df_tweets['date'] + '00'

# convert date from string to datetime
df_tweets['date'] = pd.to_datetime(df_tweets['date'])

# find and drop strange data in user_favourites
df_tweets = df_tweets[pd.to_numeric(df_tweets['user_favourites'], errors='coerce').notnull()]
df_tweets['user_favourites'] = pd.to_numeric(df_tweets['user_favourites'])

# convert text to sentimental value
# analyzer = SentimentIntensityAnalyzer()
# sentiments = []
# sentences = df_tweets['text'].tolist()
# for sentence in sentences:
#      vs = analyzer.polarity_scores(sentence)
#      sentiments.append(str(vs['compound']))

# df_tweets['sentimental_value'] = sentiments

# # drop text column
# df_tweets = df_tweets.drop(columns=['text'])

# # reindex columns
# df_tweets = df_tweets[['date', 'user_followers', 'user_favourites', 'user_verified', 'sentimental_value']]

df_tweets.info()
print(df_tweets.head())

# write to csv
#df_tweets.to_csv('revised_tweets.csv', index=False)
#print('Done')
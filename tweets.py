import pandas as pd

df_tweets=pd.read_csv('./datasets/bitcoin_tweets.csv',
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
print(df_tweets.head())
# drop unwanted columns
df_tweets = df_tweets.drop(columns=['user_name', 'user_location', 'user_description', 'user_created', 'user_friends',
   'hashtags', 'source',  'is_retweet'])

# find and drop strange data in date column
df_tweets.drop(df_tweets[(df_tweets['date'].str.len() < 19) | (df_tweets['date'].str.len() > 19)].index, inplace = True)

#print(df_tweets['date'][(df_tweets['date'].str.len() < 19) | (df_tweets['date'].str.len() > 19)])
#print(df_tweets.iloc[693194,8])

# convert date from string to datetime
df_tweets['date'] = pd.to_datetime(df_tweets['date'])
df_tweets.info()

# write to csv
#df_tweets.to_csv('revised_tweets.csv', index=False)
#print('Done')
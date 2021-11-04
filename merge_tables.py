import pandas as pd

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
df_bitstamp=pd.read_csv('bitstamp.csv', 
    dtype={
    "Timestamp": int, 
    "Open": float,
    "High": float,
    "Low": float,
    "Close": float,
    "Volume_(BTC)": float,
    "Volume_(Currency)": float,
    "Weighted_Price": float})

#df_tweets.info()
#df_bitstamp.info()

# PROCESS TWEETS
# drop unwanted columns
df_tweets = df_tweets.drop(columns=['user_name', 'user_location', 'user_description', 'user_created', 'user_friends',
    'source', 'is_retweet'])

# find and drop strange data in date column
df_tweets.drop(df_tweets[(df_tweets['date'].str.len() < 19) | (df_tweets['date'].str.len() > 19)].index, inplace = True)

#print(df_tweets['date'][(df_tweets['date'].str.len() < 19) | (df_tweets['date'].str.len() > 19)])
#print(df_tweets.iloc[693194,8])

# convert date from string to datetime
df_tweets['date'] = pd.to_datetime(df_tweets['date'])

#print(df_tweets['date'].tail(5))
#df_tweets.info()

# write to csv
#df_tweets.to_csv('revised_tweets.csv', index=False)
#print('Done')


# PROCESS BITSTAMP
# convert Timestamp from Unix int to datetime
df_bitstamp['Timestamp'] = pd.to_datetime(df_bitstamp['Timestamp'],unit='s')

# drop all rows before 2018
df_bitstamp.drop(df_bitstamp[df_bitstamp['Timestamp']<"2018-01-01"].index, inplace = True)

#df_bitstamp.info()
#print(df_bitstamp.head())

# write to csv
#df_bitstamp.to_csv('revised_bitstamp.csv', index=False)
#print('Done')
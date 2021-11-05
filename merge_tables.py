import pandas as pd

# df_tweets=pd.read_csv('./datasets/bitcoin_tweets.csv',
#     dtype={
#         "user_name": object,
#         "user_location": object,
#         "user_description": object,
#         "user_created": object,
#         "user_followers": float,
#         "user_friends": object,
#         "user_favourites": object,
#         "user_verified": object,
#         "date": "string",
#         "text": object,
#         "hashtags": object,
#         "source": object,
#         "is_retweet": object
#     })
df_bitprice=pd.read_csv('./datasets/bitcoin_price.csv',
    dtype={
    "Open Time": "string", 
    "Open": float,
    "High": float,
    "Low": float,
    "Close": float,
    "Volume": float,
    "Close Time": "string",
    "Quote asset volume": float,
    "Number of trades": int,
    "Taker buy base asset volume": float,
    "Taker buy quote asset volume": float})

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
#df_tweets.info()

# write to csv
#df_tweets.to_csv('revised_tweets.csv', index=False)
#print('Done')


# PROCESS BITSTAMP
# strip three zeros from unix time 
df_bitprice['Open Time'] = (df_bitprice['Open Time']).str[:-3]
df_bitprice['Close Time'] = (df_bitprice['Close Time']).str[:-3]

# convert Time from string to numeric
df_bitprice['Open Time'] = pd.to_numeric(df_bitprice['Open Time'])
df_bitprice['Close Time'] = pd.to_numeric(df_bitprice['Close Time'])

# convert Time from Unix format to datetime
df_bitprice['Open Time'] = pd.to_datetime(df_bitprice['Open Time'],unit='s')
df_bitprice['Close Time'] = pd.to_datetime(df_bitprice['Close Time'],unit='s')

# drop all rows before 2021 GAPERLU
#df_bitprice.drop(df_bitprice[df_bitprice['Open Time']<"2021-01-01"].index, inplace = True)

df_bitprice.info()
print(df_bitprice['Open Time'].head())

# rename 'Timestamp' column to 'date'
#df_bitstamp.rename(columns={'Timestamp': 'date'}, inplace=True)

# write to csv
#df_bitstamp.to_csv('revised_bitstamp.csv', index=False)
#print('Done')

# MERGING
# df = pd.merge(df_tweets, df_bitstamp, on='date', how='left')
# df.info()
# print(df.isnull().sum())
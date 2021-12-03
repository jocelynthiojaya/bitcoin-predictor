import pandas as pd

# read final bitcoin price 
df_bitcoin_price = pd.read_csv('datasets/final_bitcoin_price.csv',
    )
# rename column 'Date' to 'date'
df_bitcoin_price.rename(columns={'Date': 'date'},inplace=True)
df_bitcoin_price.info()


# read final tweets
df_tweets = pd.read_csv('datasets/final_tweets.csv')
df_tweets.info()

# MERGING
df = pd.merge(df_tweets, df_bitcoin_price, on='date')
df.info()
# checking null data:
print(df.isnull().sum())

# sort the value by date
df.sort_values(by='date',inplace=True)
print(df.head(30))


# export to csv
df.to_csv('datasets/merge.csv', index=False)
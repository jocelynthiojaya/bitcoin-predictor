import pandas as pd

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

# PROCESS BITSTAMP
# close time drop aja
# strip three zeros from unix time because it is wrong
df_bitprice['Open Time'] = (df_bitprice['Open Time']).str[:-3]
df_bitprice['Close Time'] = (df_bitprice['Close Time']).str[:-3]

# convert Time from string to numeric
df_bitprice['Open Time'] = pd.to_numeric(df_bitprice['Open Time'])
df_bitprice['Close Time'] = pd.to_numeric(df_bitprice['Close Time'])

# convert Time from Unix format to datetime
df_bitprice['Open Time'] = pd.to_datetime(df_bitprice['Open Time'],unit='s')
df_bitprice['Close Time'] = pd.to_datetime(df_bitprice['Close Time'],unit='s')

#df_bitprice.info()
#print(df_bitprice['Open Time'].head())

# rename 'Timestamp' column to 'date'
#df_bitstamp.rename(columns={'Timestamp': 'date'}, inplace=True)

# write to csv
#df_bitprice.to_csv('revised_bitcoin_price.csv', index=False)
#print('Done')
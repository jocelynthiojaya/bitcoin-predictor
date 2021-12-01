import pandas as pd
import numpy as np

df_bitprice=pd.read_csv('bitcoin_price.csv',
    dtype={
    "Open Time": "string", 
    "Close": float
    })

# PROCESS BITSTAMP
# close time drop aja
# strip three zeros from unix time because it is wrong
df_bitprice['Open Time'] = (df_bitprice['Open Time']).str[:-3]


# convert Time from string to numeric
df_bitprice['Open Time'] = pd.to_numeric(df_bitprice['Open Time'])


# convert Time from Unix format to datetime
df_bitprice['Open Time'] = pd.to_datetime(df_bitprice['Open Time'],unit='s')

# Checking the timestamp if its correct
print(df_bitprice['Open Time'].head())


# creating diff column to see the difference in price for the close time 
df_bitprice['diff'] = df_bitprice['Close'].diff()

# check if column is inputted
df_bitprice.info()


# Make a new column to classified whethere the price is going up or down 

    #setting up conditions
conditions = [
    (df_bitprice['diff'] < 0),
    (df_bitprice['diff'] > 0)
    ]

    # setting up the value 
values = [0,1]

    # create a new column and use np.select to assign values to it using our lists as arguments
df_bitprice['is_positive'] = np.select(conditions, values)




# Dropping unnesecary column for buildin predictive model
df_bitprice = df_bitprice.drop(
    ["Open","High","Low","Volume","Quote asset volume",
    "Number of trades", "Taker buy base asset volume", 
    "Taker buy quote asset volume","diff", "Close Time"],
    axis=1)

# Renaming OpenTime into Date column
df_bitprice.rename(columns={'Open Time': 'Date'},inplace=True)


print(df_bitprice.head())

# Write to CSV
df_bitprice.to_csv('datasets/bitcoin_price_clean.csv', index=False)
print("Done")

import pandas as pd
import data_pipeline_helper as dph

df = pd.read_csv(r"D:\codvede\stock prices data set.csv")

clean = dph.remove_null_values(df,columns=df.columns)

clean1 = dph.remove_duplicates(clean)

if "symbol" in clean1.columns:
    clean1['symbol']= clean1['symbol'].str.strip().str.upper()


if 'date' in clean1.columns:
    clean1['date'] = pd.to_datetime(clean1['date'], errors= "coerce", dayfirst=True)

    clean1 = clean1.sort_values(by=['date'])

clean1.to_csv(r"d:\codvede\clean data\clean_stock_prices_data_set.csv")



print("Before cleaning:", df.shape)
print("After cleaning:", clean1.shape)
print(clean1.dtypes)

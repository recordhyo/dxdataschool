


import pandas as pd


df = pd.read_csv('./0811python/data/seoul.csv', encoding='ms949')
#print(df.info())
print(df.head())

df.plot()

#df['avg'].plot(kind='bar')
# %%

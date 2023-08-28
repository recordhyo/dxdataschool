import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start = datetime.datetime(2023,1,1)
end = datetime.datetime(2023,8,22)

symbols = ["SPASTT01USM661N","SPASTT01KRM661N","SPASTT01JPM661N","SPASTT01EZM661N"]

data = pd.DataFrame()

for s in symbols :
    data[s] = web.DataReader(s, data_source='fred', start='2010-01-01', end='2023-08-22')[s]

#print(data.info())

data.columns = ['미국','한국','일본','유럽']
data - data/data.iloc[0] * 100
styles = ['b--', 'g--', 'c', 'r-']
data.plot(style = styles)
plt.title('세계 각국의 주가')
plt.show()
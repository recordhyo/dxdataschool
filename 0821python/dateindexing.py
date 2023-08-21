import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
#그래프에서 한글 사용하기 위한 설정
if platform.system() == 'Darwin' :
    rc('font', family ="AppleGothic")
elif platform.system() == 'Windows' :
    font_name = font_manager.FontProperties(fname='C:\Windows\Fonts\malgun.ttf').get_name()
    rc('font', family = font_name)
#음수를 사용하기 위한 설정
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('./0821python/data/stock-data.csv')
df['NewDate'] = pd.to_datetime(df['Date'])
df.set_index('NewDate', inplace=True)

#날짜 일부분을 가지고 인덱싱 가능
df_y = df['2018']
print(df_y.head())

df_y = df.loc['2018-07']
print(df_y.head())

#범위로 인덱싱 가능
df_y = df.loc['2018-06-01':'2018-06-30']
print(df_y.head())

#원하는 컬럼 범위 선택 가능
df_y = df.loc['2018-06-01':'2018-06-30','Start':'Low']
print(df_y.head())
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
#print(df.head())
#print(df.info())


#날짜 자료형으로 변경해서 새로운 필드로 저장 
df['NewDate'] = pd.to_datetime(df['Date'])
#print(df.info())

#새로만들어진 날짜 컬럼을 인덱스로 지정하고 기존 날짜 컬럼 삭제
df.set_index('NewDate', inplace=True)
df.drop('Date', axis=1, inplace=True)
print(df.head())


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


#student.csv 파일 읽기 - 이름을 인덱스로 사용

df = pd.read_csv('./0817python/data/student.csv', index_col='이름', encoding='ms949')
#print(df)

df.plot(kind='bar')
plt.show()

#단순 표준화 작업만으로는 성적을 비교한느 것이 어려울 수 있음 
#최대값이나 최대값-최소값으로 나눈 데이터로는 비교하기가 어려움
#이런 경우에는 표준값이나 편차값을 구해서 비교하는 것이 좋음

#평균과 표준편차 구하기
kormean, korstd = df['국어'].mean(), df['국어'].std()
matmean, matstd = df['수학'].mean(), df['수학'].std()
engmean, engstd = df['영어'].mean(), df['영어'].std()

#표준값 구하기
df['국어표준값'] = (df['국어'] - kormean)/korstd
df['수학표준값'] = (df['수학'] - matmean)/matstd
df['영어표준값'] = (df['영어'] - engmean)/engstd

#편차값 구하기
df['국어편차값'] = df['국어표준값'] * 10 + 50
df['영어편차값'] = df['영어표준값'] * 10 + 50
df['수학편차값'] = df['수학표준값'] * 10 + 50


df[['국어편차값','수학편차값','영어편차값']].plot(kind='bar')
plt.show()
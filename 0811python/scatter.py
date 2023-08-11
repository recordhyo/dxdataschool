import numpy as np
import pandas as pd
#matplot기반의 그래프에서 한글을 사용하기 위한 셋팅
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

if platform.system() == 'Darwin' :
    rc('font', family = 'AppleGothic')
elif platform.system() == 'Windows' :
    font_name = font_manager.FontProperties(
        fname = 'C:\Windows\Fonts\malgun.ttf').get_name()
    rc('font', family=font_name)

'''
df = pd.read_csv('./0811python/data/student.csv', encoding='ms949')

plt.figure()
#색상 설정
colormap = df.index
plt.scatter(x = df.index, y = df['국어'], marker='s', c=colormap)

plt.xticks(range(0, len(df['국어']),1), df['이름'], rotation = 'horizontal')

plt.colorbar()
plt.title('학생별 국어 점수 분포')

plt.show()
'''

#여러개 컬럼을 이용한 산포도
df = pd.read_csv('./0811python/data/noheader_auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders','displacement','horsepower','weight','accel','model year','origin','name']
#print(df.head())

#존재하지 않는 컬럼 입력시 컬럼 추가됨
df['cylinders_size'] = df['cylinders'] / df.cylinders.max() * 300
#print(df.head())
colormap = df.index
plt.scatter(x=df['weight'], y = df['mpg'], s=df['cylinders_size'], c=colormap, alpha=0.5)
plt.title('중량과 연비의 관계')
plt.show()
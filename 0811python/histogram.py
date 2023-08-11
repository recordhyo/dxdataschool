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
#첫 행이 컬럼 이름, 구분자는 쉼표, 한글 있음
df = pd.read_csv('./0811python/data/lovefruits.csv', encoding='ms949')
print(df)

data = df['선호과일'].value_counts(sort=False)

plt.hist(df['선호과일'])
plt.show()
'''

df = pd.read_csv('./0811python/data/student.csv', encoding='ms949')
#print(df)

#점수처럼 여러 값이 존재하는 경우 구간별로 히스토그램 그리는 것이 좋음
plt.hist(df['수학'], bins=3)
plt.show()
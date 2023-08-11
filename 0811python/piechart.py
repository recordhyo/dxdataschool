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


df = pd.read_csv('./0811python/data/noheader_auto-mpg.csv', header=None)
df.columns = ['mpg', 'cylinders','displacement','horsepower','weight','accel','model year','origin','name']
#중점으로부터 떨어뜨리는 비율
explode = (0.1,0.1,0.1,0.1,0.1)
x = df['cylinders'].value_counts()
plt.pie(x, labels=x.index, autopct='%1.1f%%', explode=explode)
plt.show()
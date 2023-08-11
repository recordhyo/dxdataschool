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
df = pd.read_csv('./0811python/data/student.csv', encoding='ms949')

plt.boxplot([df['국어'], df['영어'], df['수학']], labels=('국어', '영어', '수학'))
plt.show()
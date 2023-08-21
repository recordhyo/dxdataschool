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

#첫번째 데이터 - 날짜로 변경 가능, 두번째 데이터 -날짜로 변경 불가능
date_strings = np.array([
    '03-04-2005 11:35 PM',
    '04-09-2005 09:09 TM'])

#errors = 'ignore' - 예외발생시 문자열 그대로 저장(권장X)
#errors = 'coerce' - 변환 안되는 경우 NaT로 설정
#errors = 'raise' - default 값, 변환안되는 경우 예외 발생
print([pd.to_datetime(date, format='%d-%m-%Y %I:%M %p', errors='coerce') for date in date_strings])
import pandas as pd
import numpy as np

time_index = pd.date_range('01-01-2023', periods=5, freq='M')
df = pd.DataFrame(index=time_index)
df['Sales'] = [1.0, 2.0, np.nan, np.nan, 5.0]
print(df)

#앞의 데이터로 채우기
print(df.ffill())

#선형 보간
print(df.interpolate())

#비선형 보간
print(df.interpolate(method='quadratic'))

df['Stock_price'] = [1,2,3,4,5]

#단순 이동 평균
print(df.rolling(window=3).mean())

#지수 이동 평균
print(df.ewm(span=3).mean())
import pandas as pd
import numpy as np
from sklearn import preprocessing

auto_mpg = pd.read_csv('./0817python/data/auto-mpg.csv', header=None)
auto_mpg.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name'] 

#?를 None으로 치환
auto_mpg['horsepower'].replace('?', np.nan, inplace=True) 
#제거한 후 
auto_mpg.dropna(subset=['horsepower'], axis=0, inplace=True)
#자료형 변환
auto_mpg['horsepower'] = auto_mpg['horsepower'].astype('float') 

#스케일링을 수행할 데이터 가져오기
x = auto_mpg[['horsepower']].values
#print(x)

print("평균: ", np.mean(x))
print("표준편차: ", np.std(x))
print("최대값: ",np.max(x))
print("최소값: ", np.min(x))

scaler = preprocessing.StandardScaler()

#scaler.fit(x) 합쳐서 fit_transform 사용 가능
#x_scaled = scaler.transform(x)
x_scaled = scaler.fit_transform(x)


print("평균: ", np.mean(x_scaled))
print("표준편차: ", np.std(x_scaled))
print("최대값: ",np.max(x_scaled))
print("최소값: ", np.min(x_scaled))
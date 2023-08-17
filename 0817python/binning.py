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

''' ---------------------------------------------------------------------------

#pandas cut 이용

#auto_mpg의 horsepower를 3개의 구간으로 분할 
#print(auto_mpg['horsepower'].describe())

#경계값 찾기
count, bin_dividers = np.histogram(auto_mpg['horsepower'], bins=3)
#print(count, bin_dividers)

bin_names = ['저출력','보통출력','고출력']
auto_mpg['hp_bin'] = pd.cut(x= auto_mpg['horsepower'], bins=bin_dividers, labels=bin_names, include_lowest=True)
print(auto_mpg[['horsepower','hp_bin']])

---------------------------------------------------------------------------

#numpy digitize 이용

result = np.digitize(auto_mpg['horsepower'], bins=[107.33333333,168.66666667,230.0], right=True)
print(result)
#numpy에서는 그룹의 명칭을 설정하지 않고 0,1,2 처럼 인덱스로 구분함

---------------------------------------------------------------------------

#sklearn의 bining(구간 분할)
age = np.array([[13],[30],[67],[36],[20],[33],[27],[19]])
binarizer = preprocessing.Binarizer(threshold=30.0)
result = binarizer.transform(age)
print(result)

#여러개의 그룹으로 분할

#encode가 ordinal이면 일련번호로 그룹이 생성
    #onehot 을 설정하면 onehot encoding 한 후 희소 행렬로
    #onehot-dense 설정하면 onehot encoding 한 후 밀집 행렬로
kb = preprocessing.KBinsDiscretizer(4, encode='onehot', strategy='quantile')
result = kb.fit_transform(age)
print(result)

---------------------------------------------------------------------------'''

#군집 분석을 이용한 구간 분할
from sklearn.cluster import KMeans

sample = np.array([[13,30],[30,40],[12,64],[22,11],[16,95]])
df = pd.DataFrame(sample, columns=['feature1', 'feature2'])
#print(df)

#3개의 군집으로 분할하는 객체 생성
cluster = KMeans(3, random_state=42)
#sample 데이터를 이용해서 훈련
cluster.fit(sample)
#sample 데이터를 가지고 예측 
df['group'] = cluster.predict(sample)
print(df)
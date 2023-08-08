import numpy as np
import pandas as pd 

#DataFrame 생성을 위한 dictionary 생성
items = {
    'code' : [1,2,3,4],
    'name' : ['수박', '사과', '자두', '포도'],
    'price' : [30000,1500,3000,10000]
}

df = pd.DataFrame(items)
print(df)

print(df.index)
print(df.columns)

df.index = range(1,5)
df.columns = ['코드', '이름', '가격']
print(df)

#데이터 개수 많을 때 제대로 불러져 왔는지 확인할 때 사용
print(df.head(3))
print(df.tail(2))

#머신러닝 하고자 하면 머신러닝은 numpy의 ndarray로만 가능함 
print(type(df.values))

#데이터 가져왔으면 데이터에 대한 확인을 해야함 
print(df.info())
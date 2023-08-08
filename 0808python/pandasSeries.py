import numpy as np
import pandas as pd 

series1 = pd.Series([10,20,30,40]) #인덱스 없이 0,1,2,3으로 접근하도록 생성 
series2 = pd.Series([10,20,30,40], index=["one", "two","three","four"]) #인덱스 설정

#dict를 이용해서 Series 생성
series3 = pd.Series({"one":"소녀시대", "two":"에스파","three":"뉴진스","four":"르세라핌"})

'''
print(series1)
print(series2)
print(series3)

#인덱싱
print(series3[2])
print(series3["one"])
print(series3[0:2]) #0,1만 출력. 종료위치 2는 포함되지 않음
print(series3["one":"three"]) #one, two, three 출력. 종료위치 three도 포함됨

#연산
print(series1.values) #값들만 추출
print(series1+100) #연산은 ndarray 와 동일하게 수행 - values를 가지고 연산

#함수
print(np.sum(series1))
'''

s1 = pd.Series({"one":111, "two":222,"three":333,"four":444})
s2 = pd.Series({"one":np.NaN, "three":3,"four":4, "two":2})
print(s1+s2)
import pandas as pd
import numpy as np
from sklearn import preprocessing

#다항과 교차항 생성

feature = np.array([[1,2],[4,8],[2,3],[4,2],[7,2]])

#제곱항까지의 다항을 생성 - 열의 개수가 늘어나게 됨
#회귀분석을 할 때 시간의 흐름에 따라 변화가 급격하게 일어나는 경우 또는
#데이터가 부족할 때 샘플 데이터 추가하기 위해서 사용하게 됨  
#제곱이나 곱하기는 데이터 특성 자체는 크게 변화하지 않기 때문에 사용함
polynomialer = preprocessing.PolynomialFeatures(degree=2)
result = polynomialer.fit_transform(feature)
print(result)
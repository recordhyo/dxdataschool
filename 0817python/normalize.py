import pandas as pd
import numpy as np
from sklearn import preprocessing

#정규화


feature = np.array([[1,2],[4,8],[2,3],[4,2],[7,2]])
#정규화 객체
#l1은 맨하튼 거리 - 합치면 1 
#l2는 유클리드 거리 - 각 값을 전체 데이터 제곱해서 더한 값의 제곱근으로 나눈 값
#max - 큰 값으로 나눔
normalizer = preprocessing.Normalizer(norm="l2")
l2_norm = normalizer.transform(feature)
print(l2_norm)
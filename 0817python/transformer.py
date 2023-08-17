import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.compose import ColumnTransformer

feature = np.array([[1,2],[4,8],[2,3],[4,2],[7,2]])

#데이터에 함수 적용
result = preprocessing.FunctionTransformer(lambda x : x + 1).transform(feature)
print(result)


df = pd.DataFrame(feature, columns=['feature1', 'feature2'])
#apply 이용
#print(df.apply(lambda x : x+1).values)

#컬럼별로 다르게 적용
def add_one(x) :
    return x+1

def sub_one(x) :
    return x-1

result2 = ColumnTransformer([("add_one", preprocessing.FunctionTransformer(add_one, validate=True), ['feature1']),
("sub_one", preprocessing.FunctionTransformer(sub_one, validate=True), ['feature2'])]).fit_transform(df)

print(result2)
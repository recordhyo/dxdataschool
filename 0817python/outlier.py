import pandas as pd
import numpy as np
from sklearn import preprocessing
houses = pd.DataFrame()
houses['price'] = [500000,390000,290000,5000000]
houses['rooms'] = [2,3,5,116]
houses['feet'] = [1500,2000,1300,20000]

#rooms 값이 20이상이면 이상치로 간주하고 특성을 추가
houses['outlier'] = np.where(houses['rooms']>20, 1, 0)
print(houses)

#outlier의 영향을 최소화 - 특성 변환(로그변환)
houses['log_feet'] = [np.log(x) for x in houses['feet']]
print(houses)

#outlier의 영향을 최소화 - 특성 변환(scaling)
imsi = pd.DataFrame(houses['rooms'])
scaler = preprocessing.RobustScaler()
scaler.fit(imsi)
houses['scale_rooms'] = scaler.transform(imsi)
print(houses)
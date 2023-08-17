import pandas as pd
import numpy as np
'''
#z-score를 이용해서 이상치를 판별해주는 함수
def outliers_zscore(ys) :
    threshold = 3
    mean_y = np.mean(ys)
    stdev_y = np.std(ys)
    z_scores = [(y-mean_y) / stdev_y for y in ys]
    return np.where(np.abs(z_scores) > threshold)

features = np.array([[10,10,7,6,3],[200000, 3,23,12,11]])
print(outliers_zscore(features))


#z-score를 이용해서 이상치를 판별해주는 함수
def outliers_zscore(ys) :
    threshold = 3.5
    mean_y = np.mean(ys)
    stdev_y = np.std(ys)
    z_scores = [0.6745*(y-mean_y) / stdev_y for y in ys]
    return np.where(np.abs(z_scores) > threshold)

features = np.array([[10,10,7,6,3],[20000000, 3,23,12,11]])
print(outliers_zscore(features))


def outliers_iqr(ys) :
    #1사분위수와 3사분위수 구하기
    quartile_1, quartile_3 = np.percentile(ys,[25,75])
    iqr = quartile_3 - quartile_1
    #일반적인 데이터의 하한과 상한을 구하기
    lower = quartile_1 - (iqr *1.5)
    upper = quartile_3 + (iqr *1.5)
    return np.where((ys>upper) | (ys<lower))
features = np.array([[10,10,7,6,3],[20000000, 3,23,12,11]])
print(outliers_iqr(features))
'''

#일정 비율의 데이터를 이상치로 간주하기
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import make_blobs

#10행 2열의 데이터를 중앙점을 1 으로 해서 램덤하게 생성
feature, _ = make_blobs(n_samples=10, n_features=2, centers=1, random_state=42)
print(feature)

#첫번째 행의 데이터를 이상치로 수정
feature[0,0] = 10000
feature[0,1] = 10000

#이상치 감지 객체 생성 
outlier_detector = EllipticEnvelope(contamination=0.1)
outlier_detector.fit(feature)
#이상치로 판정되면 -1을 리턴하고 그렇지않으면 1을 리턴
outlier_detector.predict(feature)

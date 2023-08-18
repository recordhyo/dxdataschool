from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
t = np.array([
    'I love korea',
    'korea i love you',
    'korea food is good',
    'germany good'
])

tfidf = TfidfVectorizer()
feature = tfidf.fit_transform(t)

#희소행렬로 출력
print(feature)

#특성 이름 확인
print(tfidf.vocabulary_)

#밀집행렬로 출력
print(feature.toarray())
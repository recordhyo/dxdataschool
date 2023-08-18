import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

t = np.array([
    'The blue folder lying on top of my desk.',
    'The theater is accessible through the mall.',
    'The man over there knows the area well.'
])

c = CountVectorizer()

bag_of_word = c.fit_transform(t)
#희소행렬의 형태로 출력됨 
#print(bag_of_word)

#특성 이름 확인
print(c.get_feature_names_out())

#밀집행렬 형태로 출력
print(bag_of_word.toarray())
#벡터화 된 함수 적용 
import numpy as np

ar = np.array([1,2,3,4,5])

#매개변수에 100을 더해서 리턴하는 함수
def f(i) :
    return i + 100

#벡터화된 함수로 수정
vector_f = np.vectorize(f)

#배열에 벡터화된 함수 적용
print(vector_f(ar))

#람다 함수 벡터화
print(np.vectorize(lambda x : x+100)(ar))
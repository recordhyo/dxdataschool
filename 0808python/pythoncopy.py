#파이썬에서의 데이터 복제
#copy 모듈의 copy(얕은 복사) 와 deepcopy(깊은 복사) 함수 이용

import copy

li = [1,2,3]
c = li.copy() #얕은 복사
c[0] = 100 #1차원 list의 경우 원본에 영향을 주지 않음
print(li)

m = [[1,2,3],[4,5,6]]
c = m.copy() #얕은 복사
c[0][0] = 100 #2차원 배열의 경우는 원본에 영향을 줌
print(m)

#deepcopy는 재귀적으로 복제를 수행하기 때문에 복사본 수정해도 원본에 영향 없음
d = copy.deepcopy(m)
d[0][0] = 1004 
print(m)
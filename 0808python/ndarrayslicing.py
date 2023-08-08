import numpy as np 

li = [1,2,3,4,5]
c = li[0:3] #list 슬라이싱 : 얕은 복사 수행
#c와 li는 앞의 3개 데이터 동일하지만 다른 공간의 데이터
print(c)
c[0] = 100 #c의 값 변경해도 li에는 영향이 없음
print(li)



ar = np.array(li)
d = ar[0:3] #vector data 이므로 참조가 복사됨
print(d)
d[0] = 100 #d의 값 수정하면 원본에 영향을 주게 됨 
print(ar)

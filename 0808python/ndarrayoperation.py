import numpy as np

#산술 연산
ar = np.array([1,2,3,4,5])
br = np.array([10,20,30,40,50])

result = ar+br
print(result)

result = ar + 4
#2개의 차원이 다른 경우 적은 차원 데이터를 큰 차원 데이터로 수정
print(result)


cr = np.array(range(1,11))
#print(ar+cr) error
#일차원 배열을 2행 5열로 수정해서 연산 수행
k = cr.reshape(2,5)
print(ar+k) 



# ----------------------------------------------------------------

#논리 연산 
ar = np.array([1,2,3,4,5])
br = np.array([10,20,False,40,0])
print(ar > br)
print(np.not_equal(ar,br))
print(np.logical_xor(ar,br)) #and, or, xor 는 bool로만 판정함


# ----------------------------------------------------------------

#연산 후 할당 가능 
ar = np.array([1,2,3,4,5])
br = np.array([10,20,False,40,0])
ar += br
print(ar)


# ----------------------------------------------------------------

#in, not in 연산자
print(1 in ar)
print([1,2] in ar)
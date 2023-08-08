import numpy as np 

li = list(range(1,11))
matrix = np.array(li).reshape((5,2))

print(matrix)

print(matrix.reshape(2,5)) #행과 열의 수를 변경

print(matrix.T) #행과 열을 변경 

print(np.transpose(matrix)) #행과 열을 변경 
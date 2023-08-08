import numpy as np 

li = list(range(1,10))
print(li)

#list 이용해서 ndarray 생성
ar = np.array(li)
print(ar)

#1차원 배열 생성 후 행과 열의 개수 3X3으로 변경
matrix = np.array(li).reshape((3,3))
print(matrix)


#인덱싱 - 데이터 1개 가져오기
data1 = ar[0]
print(data1)

#2차원 배열 - 데이터 1개 가져오기
data2 = matrix[0,0]
data3 = matrix[0][0]
print(data2)
print(data3)


#2차원 배열 - 행 하나 찾아오기
row = matrix[0] # = matrix[0][:]
print(row)

#2차원 배열 - 열 하나 찾아오기
column = matrix[:,0]
print(column)


import numpy as np 
li = list(range(1,10))
ar = np.array(li)
matrix = np.array(li).reshape((3,3))

data1 = ar[0]
data2 = matrix[0,0]
data3 = matrix[0][0]

row = matrix[0]
column = matrix[:,0]



#파이썬의 scala data는 일반적으로 immutable (변경불가능)
#scala data는 다른 변수에 대입할 때 값을 복사해서 대입함
a = 10
b = a
b = 20
print(a) #10

#파이썬의 vector data는 다른 변수에 대입할 때 참조를 복사해서 대입함
ax = [1,2,3]
bx = ax
bx[0] = 100
print(ax) #[100,2,3]


#scala data를 복사하는 경우는 원본 값 복사해서 대입하기 때문에 서로간 영향 주지 않음
data1 = 1000
print(data1)
print(ar)

data2 = 1000
print(data2)
print(matrix)

#vector data를 다른 곳에 대입하면 참조가 복사되어 복사본 수정하면 원본도 영향을 받음
row[0] = 1004
print(row)
print(matrix)

#scala data - primitive type
#vector data - non-primitive type(reference type)

#데이터 복제는 copy()메소드 - 수정해도 영향을 주지 않음
clone = matrix.copy()
clone[0][0] = 555
print(matrix)
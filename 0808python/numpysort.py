import numpy as np

#1차원 배열의 정렬
ar = np.array([20,1,46,12,53])
result = np.sort(ar) #데이터를 정렬
print(result)
print(ar) #ar은 그대로 

#2차원 배열의 행에서의 정렬
br = np.array([[10,60,80],[20,50,30],[15,55,32]])
result = np.sort(br, axis=1)
print(result)

import numpy as np

#인덱싱 할 때 list를 이용
ar = np.array([100,200,300,400,500])
f =ar[[0,2]]
print(f)
f[0] = 1004
print(ar)
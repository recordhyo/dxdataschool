import numpy as np


x = range(1,51)
ar = np.array(x).reshape((10,5))

print(ar)

cnt = ar.shape[0]
#데이터를 가지고 7:3 분할
br, cr, dr = np.split(ar,[int(cnt*0.7), int(cnt*0.9)])

print(br)
print(cr)
print(dr)
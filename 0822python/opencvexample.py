import numpy as np
import cv2
import matplotlib.pyplot as plt
'''
#opencv 이미지데이터 읽으면 numpy의 ndarray로 리턴, 흑백은 2차원 컬러는 3차원
img = cv2.imread('./0821python/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img2 = np.zeros(shape=(512,512), dtype=np.uint8) + 100

#이미지 색상값 0~255이여야하는데 덧셈하면 256이상은 256으로 나눈 나머지값 가짐

dst = cv2.add(img, img2) 
#opencv함수 이용해서 더하면 256이상의 값은 255로 설정됨

plt.imshow(dst, cmap='gray')
plt.axis('off')
plt.show()
'''

img = cv2.imread('./0822python/data/minMax.jpg', cv2.IMREAD_GRAYSCALE)

(min_v, max_v, _, _) = cv2.minMaxLoc(img)

ratio = 255 / (max_v - min_v)
dst = np.round((img-min_v)*ratio).astype('uint8')
plt.imshow(dst, cmap='gray')
plt.axis('off')
plt.show()
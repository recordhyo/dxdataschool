import cv2
import numpy as np
import matplotlib.pyplot as plt

#이미지 데이터 흑백으로 가져오기 - 2차원 배열
#C/C++이나 Python에서는 상수 정의할 때 이름을 사용한 경우 상수 대신 값을 직접 입력해도됨 
#cv2.IMREAD_GRAYSCALE 대신 0 입력해도 되지만 상수 이름 사용하는 것 권장
img = cv2.imread('./0821python/data/plane.jpg', cv2.IMREAD_GRAYSCALE)
print(img.shape)

#plt.imshow(img, cmap='gray')
#plt.axis('off')
#plt.show()

#OpenCV 이미지를 컬러로 가져오면 RGB가 아니고 BGR 순서임 
img = cv2.imread('./0821python/data/plane.jpg', cv2.IMREAD_COLOR)
print(img.shape)

#RGB로 변환
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
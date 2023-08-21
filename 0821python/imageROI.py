import cv2
import matplotlib.pyplot as plt
'''
img = cv2.imread('./0821python/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
img[100,200] = 0
img[100:400, 200:300] = 0 #이미지의 특정 부분을 선택하는것 ROI 
#이미지 전처리의 핵심중 하나 - ROI와 다른 부분 확연하게 구분되도록 하는 것
plt.imshow(img, cmap='gray')
plt.show()
'''

img = cv2.imread('./0821python/data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img[100:400, 200:300, 0] = 255 #특정 색상값 하나만 접근하는 것 - 채널접근
plt.imshow(img)
plt.show()
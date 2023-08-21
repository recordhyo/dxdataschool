import cv2
import matplotlib.pyplot as plt
'''
img = cv2.imread('./0821python/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
print("img sahape", img.shape)

#이미지 1차원으로 변경
img = img.flatten()
print("img sahape", img.shape)

#3차원으로 변경
img = img.reshape(-1, 512, 512)
#-1은 나머지를 전부 사용한다라는 의미
#262144 / 512 /512가 첫번쨰 차원
print("img sahape", img.shape)
plt.imshow(img[0], cmap='gray')
plt.axis('off')
plt.show()
'''

img = cv2.imread('./0821python/data/plane.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(128,128))
plt.imshow(img, cmap='gray')
plt.show()
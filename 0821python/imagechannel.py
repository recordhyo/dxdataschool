import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./0821python/data/lena.jpg')

#채널 분할 
b, g, r = cv2.split(img)

#채널 병합
img = cv2.merge([r,g,b])

plt.imshow(img)
plt.axis('off')
plt.show()
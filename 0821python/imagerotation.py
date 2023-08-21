import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./0821python/data/flip_test.jpg')

#img_flip = cv2.flip(img, -1) #축을 기준으로 뒤집기
#img_t = cv2.transpose(img) #행렬을 전치
#img_f = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
#img_f = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
#img_f = cv2.rotate(img,cv2.ROTATE_180)

rows, cols, channel = img.shape
#중앙을 기준으로 45회전하고 0.5배 축소한 이미지
M1 = cv2.getRotationMatrix2D((rows/2, cols/2), 45, 0.5)
#얻은 행렬로 이미지 만들기 
img_a = cv2.warpAffine(img, M1, (rows, cols))

plt.imshow(img_a)
plt.axis('off')
plt.show()
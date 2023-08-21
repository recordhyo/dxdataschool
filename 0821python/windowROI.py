import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./0821python/data/lena.jpg', cv2.IMREAD_GRAYSCALE)
roi = cv2.selectROI(img)
print('roi: ', roi)

#선택영역만 추출 
img = img[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
cv2.imshow("IMG", img)
cv2.waitKey()
cv2.destroyAllWindows() 
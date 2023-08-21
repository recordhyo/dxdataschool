import cv2
import numpy as np

#자료형을 np.uint8로 설정 - 이미지는 0~255 사이의 숫자만 이용
#이미지가 2차원이면 흑백, 3차원이면 컬러
image = np.zeros(shape=(512,512,3), dtype=np.uint8) + 255

p1 = 100,100
p2 = 400,400
#cv2.rectangle(image,p1,p2,(255,0,255),2)

#OpenCV에서는 옵션을 정수로 설정함
cv2.circle(image, (image.shape[0]//2, image.shape[1]//2),50,(0,0,255),thickness=-1)

#윈도우에 이미지 출력
cv2.imshow('image', image)
#키보드 입력 대기 
cv2.waitKey(0)
#윈도우 종료
cv2.destroyAllWindows()


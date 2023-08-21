import cv2
import numpy as np
#print(cv2.__version__)

#모든 값 200으로 채운 2차원 행렬 생성
image = np.zeros((200,400), np.uint8)
image[:] = 200

#윈도우 생성 
cv2.namedWindow('윈도우생성')
#윈도우에 이미지 출력
cv2.imshow('윈도우생성', image)
#키보드 입력 대기 
cv2.waitKey(0)
#윈도우 종료
cv2.destroyAllWindows()
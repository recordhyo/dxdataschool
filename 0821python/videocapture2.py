import cv2
import numpy as np
import matplotlib.pyplot as plt
#droidcam 설치
cap = cv2.VideoCapture('http://192.168.0.49:4747/video') #아이폰, 웹캠
#cap = cv2.VideoCapture('http://192.168.0.49:4747/mjpegfeed') 안드로이드

#카메라의 해상도 확인
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size', frame_size)

while True : 
    #스마트폰 영상 가져오기
    retval, frame = cap.read()
    if not retval :
        break

    #영상을 화면에 출력
    cv2.imshow('frame', frame)
    #키보드 대기
    key = cv2.waitKey(25)
    #ESC 누르면 종료
    if key == 27:
        break
if cap.isOpened():
    cap.release()
cv2.destroyAllWindows()
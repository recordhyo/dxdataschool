import cv2
import numpy as np
import matplotlib.pyplot as plt

def put_s(frame, text, pt, value, color=(120,200,90)):
    text += str(value)
    shade = (pt[0] +2, pt[1] +2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0,0,0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)


#현재 디바이스에 있는 첫번째 카메라 연결
capture = cv2.VideoCapture(0)

#카메라가 연결되지 않으면 종료
if capture.isOpened() == False :
    raise Exception('카메라 연결 불가')

while True : 
    #캡쳐된 데이터 가져오기
    ret, frame = capture.read()
    if not ret :
        break
    if cv2.waitKey(30) >= 0 :
        break
    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    put_s(frame, "EXPOS: ", (10,40), exposure)
    title = "capture from camera"
    cv2.imshow(title,frame)
capture.release()
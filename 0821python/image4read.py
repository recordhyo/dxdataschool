import cv2
import numpy as np
import matplotlib.pyplot as plt
#4개의 이미지 2*2로 출력

#공통된 것들을 상수화
DATA_DIR = './0821python/data/'
#같이 사용되는 것들 리스트로 묶기
imglist = []
imglist.append(cv2.imread(DATA_DIR+'lena.jpg'))
imglist.append(cv2.imread(DATA_DIR+'apple.jpg'))
imglist.append(cv2.imread(DATA_DIR+'baboon.jpg'))
imglist.append(cv2.imread(DATA_DIR+'orange.jpg'))

img_rgb_list = []
for i in imglist :
    img_rgb_list.append(cv2.cvtColor(i, cv2.COLOR_BGR2RGB))


#여러개의 영역 만들기 
fig, ax = plt.subplots(2,2, figsize=(10,10), sharey=True)

length = len(img_rgb_list)
for i in range(length) :
    ax[i//2][i%2].axis('off')
    ax[i//2][i%2].imshow(img_rgb_list[i], aspect='auto')

plt.show()

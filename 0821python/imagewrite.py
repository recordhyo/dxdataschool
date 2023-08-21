import cv2
import numpy as np
import matplotlib.pyplot as plt
#컬러 이미지를 흑백으로 저장
img = cv2.imread('./0821python/data/plane.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('./0821python/data/planegray.jpg',img)
import numpy as np
import cv2


# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)       
img2 = np.zeros((240, 320, 3), dtype=np.uint8)    
img3 = np.ones((240, 320), dtype=np.uint8) * 255  # whilte
img4 = np.full((240, 320, 3), (200, 0 , 200), dtype=np.uint8)  # yellow

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('ch02\\flower2.PNG')

img2 = img1
img3 = img1.copy()

img1.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('ch02\\flower2.PNG')

img2 = img1[20:120, 30:250]  # numpy.ndarray의 슬라이싱
img3 = img1[20:120, 30:250].copy()

cv2.circle(img2, (50,50), 20, (0,0,255),2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

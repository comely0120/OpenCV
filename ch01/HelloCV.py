import cv2
import sys

print(cv2.__version__)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

# 영상이 없을 경우의 에러처리
if img is None:
    print('Image load failed..!')
    sys.exit()

cv2.namedWindow('IMAGE')
cv2.imshow('IMAGE',img)
cv2.waitKey() # 다른 키를 누르면 이미지 창 종료

cv2.destroyAllWindows()
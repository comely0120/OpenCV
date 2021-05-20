import sys
import cv2

'''
# 마스크 영상을 이용한 영상 합성
src = cv2.imread('ch02\\airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('ch02\\mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('ch02\\field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

#cv2.copyTo(src, mask, dst)
dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
'''

# 마스크 영상을 이용한 영상 합성
src = cv2.imread('ch02\\opencv-logo-white.png', cv2.IMREAD_UNCHANGED)
mask = src[:,:,-1] # 가로, 세로 다 가져오고 마지막 체널 1개만
src = src[:,:,0:3]
dst = cv2.imread('ch02\\field.bmp', cv2.IMREAD_COLOR)


h,w = src.shape[:2]
crop = dst[0:h, 0:w]

cv2.copyTo(src,mask,crop)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

#cv2.copyTo(src, mask, dst)
#dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
import sys
import cv2


# 영상 불러오기
img1 = cv2.imread('ch02\\flower.PNG', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('ch02\\flower.PNG', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# 영상의 속성 참조
print('type(img1):', type(img1))
print('img1.ndim:', img1.ndim)
print('img2.ndim:', img2.ndim)
print('img1.shape:', img1.shape)
print('img2.shape:', img2.shape)
print('img1.dtype:', img1.dtype)


# 영상의 크기 참조
h,w = img1.shape
print('img1 size: {} x {}'.format(w, h))

h, w = img2.shape[:2]
print('img2 size: {} x {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

# 영상의 픽셀 값 참조
x = 20
y =10

p1 = img1[y,x]
print('p1',p1)

p2 = img2[y,x]
print('p2',p2)

for y in range(h):
    for x in range(w):
        img1[y, x] = 0
        img2[y, x] = (0, 200, 0)        


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()

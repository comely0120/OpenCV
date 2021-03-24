import sys
import glob
import cv2

# 이미지 파일 불러와서 img_files에 추가
img_files = glob.glob('ch01\\slideimg\\*.JPG')

if not img_files:
    print("There are no jpg files in 'slideimg' folder")
    sys.exit()

# 전체 화면으로 'SlidShow' 창 생
cv2.namedWindow('SlideShow', cv2.WINDOW_NORMAL)
cv2.setWindowProperty("SlideShow", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)


cnt = len(img_files) # 불러온 이미지 개수
idx = 0
while True:
    img = cv2.imread(img_files[idx])
    
    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('Slideshow', img)
    
    # 종료 조건 => ESC(27)키를 누르면 종료
    if cv2.waitKey(1000) == 27 : 
        break
    
    # 다음사진으로 넘어가기. 마지막 사진이면 idx=0으로 두어 처음 사진으로 다시돌아가기
    idx += 1
    if idx >= cnt :
        idx =0

cv2.destroyAllWindows()
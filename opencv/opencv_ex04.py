import cv2
import numpy as np

org = cv2.imread('./image/티모.jpeg', cv2.IMREAD_GRAYSCALE) # 이미지 로드
dst = cv2.resize(org, dsize=(640, 480))

# center = [144, 199] # x,y
# color = (0, 0, 255) # red

# cv2.circle(dst, tuple(center), 30, color)

cv2.imshow('dest', dst) # 이미지 잘 띄우기

cv2.waitKey(0)  # 키 대기
cv2.destroyAllWindows() # OpenCV 인스턴스 종료


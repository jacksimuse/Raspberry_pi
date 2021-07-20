import cv2
import numpy as np #  C#의 리스트, 행렬이 포함되어 있지 않아, numpy

# 이미지 로드 기본툴
org = cv2.imread('./image/timo.jpeg') # 이미지가 크다면 주소 다음에 , cv2.IMREAD_REDUCED_COLOR_2
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
blur = cv2.blur(org, (10, 10)) # 블러 뿌옇게하기
kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
sharp = cv2.filter2D(org, -1, kernel)

cv2.imshow('Original', org) # 이미지를 새창에 띄우기
cv2.imshow('Blur', blur)
cv2.imshow('Sharp', sharp) # 선명하게

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제
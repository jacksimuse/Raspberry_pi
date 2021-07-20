import cv2
import numpy as np #  C#의 리스트, 행렬이 포함되어 있지 않아, numpy

# 이미지 로드 기본툴
org = cv2.imread('./image/timo.jpeg') # 이미지가 크다면 주소 다음에 , cv2.IMREAD_REDUCED_COLOR_2
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape
#노이즈 추가
noise = np.uint8(np.random.normal(loc=0, scale=80, size=[h, w, c]))
noised_img = cv2.add(org, noise) # 원본 이미지에 노이즈 추가

cv2.imshow('Original', org) # 이미지를 새창에 띄우기
cv2.imshow('noise', noise)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제
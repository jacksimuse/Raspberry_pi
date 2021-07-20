import cv2
import numpy as np #  C#의 리스트, 행렬이 포함되어 있지 않아, numpy

# 이미지 로드 기본툴
org = cv2.imread('./image/timo.jpeg') 
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape
print('Width:{0}, Height:{1}, Channel:{2}'.format(w, h, c))
size_small = cv2.resize(gray, dsize=(int(w/2), int(h/2))) # 사이즈 반으로 변경

cv2.imshow('Original', org) # 이미지를 새창에 띄우기
cv2.imshow('Gray', gray)
cv2.imshow('Resize', size_small)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제
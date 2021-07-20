import cv2
import numpy as np #  C#의 리스트, 행렬이 포함되어 있지 않아, numpy

# 이미지 로드 기본툴
org = cv2.imread('./image/timo.jpeg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
# 이미지 대비
enhanced = cv2.equalizeHist(gray)

cv2.imshow('Original', org) # cv2 새창 열림
cv2.imshow('Enhance', enhanced)

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제
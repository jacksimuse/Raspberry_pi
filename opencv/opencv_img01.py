import cv2
import numpy as np #  C#의 리스트, 행렬이 포함되어 있지 않아, numpy

# 이미지 로드 기본툴
org = cv2.imread('./image/timo.jpeg')

cv2.imshow('Original', org) # cv2 새창 열림
cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제
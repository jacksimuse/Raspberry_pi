import cv2
import numpy as np #  C#의 리스트, 행렬이 포함되어 있지 않아, numpy

# 이미지 로드 기본툴
org = cv2.imread('./image/timo.jpeg') # 이미지가 크다면 주소 다음에 , cv2.IMREAD_REDUCED_COLOR_2
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)

h, w, c = org.shape
# 그림 자르기
cropped = org[:, :int(w/2)] # 아래를 자르려면 앞쪽:int(h/2) 옆을 자르려면 뒷쪽:int(w/2) 에 자르고 싶은걸 넣어준다

cv2.imshow('Original', org) # 이미지를 새창에 띄우기
cv2.imshow('Cropped', cropped) # 반으로 자른 이미지

cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제
import cv2
import numpy as np #  C#의 리스트, 행렬이 포함되어 있지 않아, numpy

# 이미지 로드 기본툴
org = cv2.imread('./image/timo.jpeg')
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
ret, bny = cv2.threshold(gray, 127, 255, 0)
cont, hirc = cv2.findContours(bny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(org, cont, 0, (0, 255, 0), 2)
cv2.imshow('result', org)


cv2.waitKey(0) # 창에서 키입력 대기
cv2.destroyAllWindows() #메모리 해제
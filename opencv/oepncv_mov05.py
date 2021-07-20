import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image

# 카메라 기본 틀
cap = cv2.VideoCapture(0) # 번호 0부터 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./Fonts/NanumGothicBold.ttf', 20)


# 무한루프 지정 키를 눌렀을 때
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret Ture/False
    frame = cv2.flip(frame, 0)

    h, w, _ = frame.shape # channel은 불필요
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')

    if ret != True: break # ret이 False면 루프탈출

    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    draw.text(xy=((w-300), 10), text="겸's_TV - {0}".format(currDateTime), font=font, fill=(0, 0, 255))
    frame = np.array(frame) # 웹상태 복귀

    #cv2.imshow('RealTime cam', frame)   # 로드한 영상을 창에 띄움
    cv2.imshow('Gray Result', frame)

    if cv2.waitKey(1) == ord('q'): # q를 입력하면 루프탈출
        break

cap.realse() # 웹캠해제
cv2.destroyAllWindows()
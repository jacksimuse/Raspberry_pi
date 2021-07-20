import cv2
import numpy as np
import datetime
from PIL import ImageFont, ImageDraw, Image
from numpy.core.records import fromrecords
from numpy.lib.type_check import isreal

# 카메라 기본 틀
cap = cv2.VideoCapture(0) # 번호 0부터 
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# 나눔고딕볼드 로드
font = ImageFont.truetype('./Fonts/NanumGothicBold.ttf', 20)

# 영상 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
is_record = False

# 무한루프 지정 키를 눌렀을 때
while True:
    ret, frame = cap.read() # 카메라 현재 영상 로드, frame에 저장, ret Ture/False
    frame = cv2.flip(frame, 0)

    h, w, _ = frame.shape # channel은 불필요
    now = datetime.datetime.now()
    currDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
    fileDateTime = now.strftime('%Y%m%d_%H%M%S') # 20210720_164725  캡쳐되는 파일 이름

    if ret != True: break # ret이 False면 루프탈출

    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    draw.text(xy=((w-300), 10), text="겸's_TV - {0}".format(currDateTime), font=font, fill=(0, 0, 255))
    frame = np.array(frame) # 웹상태 복귀

    #cv2.imshow('RealTime cam', frame)   # 로드한 영상을 창에 띄움
    cv2.imshow('Gray Result', frame)

    key = cv2.waitKey(1)
    if key == ord('q'): break# q를 입력하면 루프탈출
    elif key == ord('c'): #c는 화면캡쳐
        cv2.imwrite('./capture/img_{0}.png'.format(fileDateTime), frame)
        print('이미지 저장 완료')
    elif key == ord('r'): # 레코드 시작
        is_record = True
        video = cv2.VideoWriter('./capture/record_{0}.avi'.format(fileDateTime), fourcc, 20, (w, h))
        print('녹화 시작')
    elif key == ord('t'): # 레코드 종료
        is_record = False
        video.release() # 객체 해제
        print("녹화 완료")

    if is_record:
        video.write(frame)
        cv2.circle(img=frame, center=(620, 15), radius=5, color=(0, 0, 255), thickness=3)
cap.realse() # 웹캠해제
cv2.destroyAllWindows()
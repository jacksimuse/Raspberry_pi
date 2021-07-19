import cv2

cam = cv2.VideoCapture(0)   # 기본 웹
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 창 넓이
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 창 높이
while True: 
    ret, frame = cam.read() #웹캠 열기
    frame = cv2.flip(frame, 0) 

    if ret:
        cv2.imshow('CAM', frame)    # 카메라 영상 CAM이라는 이름으로 창에 띄움

    key = cv2.waitKey(1) # q를 입력받으면
    if  key == ord('q'):
        break 

cam.release()
cv2.destroyAllWindows()

# 원격 접속
원격 접속은 telnet과 SSH프로그램을 이용하여 텍스트 터미널 모드에서 원격으로 리눅스 시스템에 접속하는 방법이 있다.

라즈베리 파이를 위한 SD카드를 만들 당시 SSH파일을 넣었기 때문에 SSH로 접속하는 방법으로 실행했다.
PuTTY로 접속하기 전 원활한 와이파이를 위해 공유기를 설치하였고 각자 라즈베리파이 IP에 외부포트와 내부포트를 할당해주었다.
### 포트설정
![image](https://user-images.githubusercontent.com/73567433/125270153-59deff80-e344-11eb-881c-a54c5d99a846.png)

### PuTTY 실행
![image](https://user-images.githubusercontent.com/73567433/125270238-6cf1cf80-e344-11eb-8105-19f402fdd252.png)

## 그래픽 모드 접속
VNC는윈도우와 같이 리눅스를 사용하기 편한 UI로 보여주는 디스플레이 서버이다.
PuTTY를 실행한 후 ID와 PassWord를 입력후 터미널에 vncserver를 치고 VNC VIEWER를 통해 접속할 수 있다.
접속하기 전 VNC서버 설치를 하기 위해 명령을 해 줘야한다.
```linux
$ sudo apt-get install realvnc-vnc-server
```
리눅스 터미널과 같이 VIEWER에서 ID와 PassWord를 치고 접속 하면된다.
![image](https://user-images.githubusercontent.com/73567433/125271915-32893200-e346-11eb-81d2-1e0e40bc7c12.png)

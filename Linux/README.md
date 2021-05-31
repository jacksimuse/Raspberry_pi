# 리눅스 환경

- 리눅스에는 셸과 프롬포트가 있다.
- 셸은 커널의 바깥쪽에 위치하며 사용자와 커널 사이의 인터페이스를 제공한다.
- 프롬포트는 pi@raspberrypi: ~ $ 라는 글씨가 보이고 $ 문자 뒤에 작은 블록이 표시 되면서 입력을 기다린다.
- 리눅스는 bash를 사용한다.

## 알아두면 좋은 리눅스의 기본 명령어

1. 리눅스의 주요 명령어
  - ls : 디렉터리 목록 표시
  - clear : 화면지우기
  - echo : 인수로 지정한 문자열을 그대로 출력
  - cp : 파일 복사
  - rm : 파일 삭제
  - mv : 파일 이동
  - cd : 디렉터리 이동
  - mkdir : 디렉터리 생성
  - rmdir : 디렉터리 삭제
  - pwd : 현재 작업중인 디렉터리의 경로를 표시한다.
  - cat : 파일의 내용 표시
  - find : 파일명을 이용하여 시스템에서 파일을 찾는다.
  - which : 명령어가 위치하고 있는 경로를 표시한다
  - sudo : 다른 사용자의 보안 권한으로 명령어를 수행한다.
  - chmod: 파일의 접근 권한을 변경한다.
  - reboot : 시스템 재시작
  - apt-get 데비안에서 소프트웨어 패키지를 설치 및 관리한다.
2. 명령어 사용방법
  $ 명령어 [옵션] [파일명]
  ex) ls --help / info ls / man ls
* 옵션
  - -l : 파일에 대해서 권한이나 생성시간처럼 보다 자세한 내용을 출력한다
  - -a : 숨긴 파일이나 디렉터리 등의 현재 디렉터리의 모든 내용을 출력한다.
  - -h : 파일의 크기를 K, M, G와 같이 사람이 읽기 편한 단위로 출력한다.
  - -F : 실행 파일이나 디렉터리 등이 쉽게 구분될 수 있도록 출력한다.
  - -R : 하위 디렉터리의 내용도 함께 출력한다
 
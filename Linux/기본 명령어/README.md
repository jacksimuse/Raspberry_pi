# 기본 명령어

리눅스는 주로 bash(bourne again shell)를 사용한다.
셸 명령어는 보통 다음과 같은 형식이다.

명령어 [-옵션] 매개변수...
ex)
```Linux
$ ls -l python_games
```

## 파일 목록 보기(ls)
현재 디렉터리의 파일 목록을 보여 주는 가장 기본적이 명령어다.

ls명령어 형식
|일반 형식| ls［-aCxdlstucriFR］(files_name)|
|------|------|
|-a|모든 파일을 출력한다.|
|-l|각 파일에 대한 종류, 소유자, 권한, 갱신일 등의 자세한 정보를 보여준다.|
|-t|최근에 만들어진 파일 순서로 보여 준다.|
|-R|하위 디렉터리의 내용까지 전부 보여준다.|
|-i|파일의 inode 번호를 보여 준다.|
|-u|엑세스(access)한 날짜 순서대로 정렬한다.|
|-r|정렬된 순서의 역으로 출력한다.|

## 경로와 현재 작업 디렉터리 및 변경(pwd, cd)
pwd(print working directory)는 현재 디렉터리, 즉 현재 작업 디렉터리를 출력한다.
cd(change directory)는 현재 작업 디렉터리를 변경하는 명령어다.
예시
```linux
pi@raspberrypi ~ $ pwd
/home/pi
pi@raspberrypi ~ $ cd ~/Downloads
pi@raspberrypi ~/Downloads $ pwd
/home/pi/Downloads
pi@raspberrypi ~/Downloads $ cd /home/pi
pi@raspberrypi ~ $ pwd
/home/pi
```
여기서 '~'는 사용자의 홈 디렉터리를 나타낸다. 또한 cd명령에서 디렉터리 이름을 주지 않고 실행하면 홈 디렉터리로 이동한다.

## 파일 처리 명령어(touch)
1. touch : 본래 파일 수정 시간을 갱신하는 명령이지만, 파일이 존재하지 않는 경우엔 빈 파일을 생성시킨다.
```linux
pi@raspberrypi ~/Test $ touch catTest.txt
pi@raspberrypi ~/Test $ ls -la catTest.txt
-rw-r--r-- 1 pi pi 0 2월 11일 16:13 catTest.txt
```
2. cat : 표준 출력 재지향 기호'>'와 함께 쓰면 키보드로부터 입력받은 내용을 파일로 저장할 수 있다. 여기서 입력을 끝낸 후 Ctrl+D 키를 입력해야 파일이 저장되고 셸로 돌아오게된다.
```linux
pi@raspberrypi ~ $ cat > catTest.txt
Hello!
^D
pi@raspberrypi ~ $
```
3. cp : 파일을 현재의 위치 또는 다른 디렉터리로 복사한다. 만약 파일이 존재한다면 기존에 있던 파일은 사라지고 새로운 복사본 파일로 바뀐다.
```linux
pi@raspberrypi ~ $ ls
Desktop Downloads python_games Test
pi@raspberrypi ~ $ cp /bin/date Test
pi@raspberrypi ~ $ cd Test
pi@raspberrypi ~/Test $ ls
catTest.txt date
```
|일반 형식| cp［-abdfilPprsuvxR］files_name1 file_name2|
|------|------|
|-a|가능한 한 원래 파일의 구조와 속성을 그대로 복사한다.|
|-R|디렉터리를 재귀적으로 복사한다.|
|-b|복사할 때 덮어쓰게 되는 파일은 백업을 만든다.|
|-P|원본 파일의 소유자, 그룹, 권한, 시간 기록을 그대로 복사한다.|
|-d|심벌릭 링크는 심벌릭 링크로 복사한다. 그리고 원본 파일과의 하드 링크 관계를 유지한다.|
|-f|복사 위치에 존재하는 파일을 제거하고 복사한다.|
4. rm : 파일을 삭제한다.
|일반 형식| ls［-aCxdlstucriFR］(files_name)|
|------|------|
|-f|지울 파일이 있을 경우 강제로 삭제한다.|
|-i|지울 파일이 있을 경우 지울 것인지 물어본다.|
|-r|하위 디렉터리에 있는 모든 파일을 삭제한다.|
|-v|지우는 파일 정보를 출력한다.|
5. mv : 파일을 이동하거나 이름을 변경하는 명령어다.
|일반 형식| ls［-aCxdlstucriFR］(files_name)|
|------|------|
|-b|대상 파일이 지워지기 전에 백업 파일을 만든다.|
|-f|대상 파일의 접근 허가와 관계없이 무조건 파일을 이동한다.|
|-i|대상 파일이 기존 파일이면, 덮어쓸 것인지 물어본다.|
|-u|대상 파일보다 원본 파일이 최근의 것일 때 업그레이드 한다.|
|-v|파일 옮기는 과정을 자세하게 보여준다.|
6. mkdir : 디렉터리를 생성하는 명령이다.
|일반 형식| ls［-aCxdlstucriFR］(files_name)|
|------|------|
|-m|새로운 디렉터리의 허가 모드를 지정한 모드로 설정한다.|
|-p|부모 디렉터리가 존재하지 않는 경우 자동으로 생성한다.|


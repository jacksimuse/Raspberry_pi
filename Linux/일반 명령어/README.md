# 일반 명령어
### 1. 도움말 보기(man)

각종 시스템 명령어들의 도움말 또는 매뉴얼을 출력해 준다. 출력되는 매뉴얼은 매우 자세한 설명을 포함한다.

|일반 형식| man［-s］파일명1 파일명2|
|------|------|
|옵션|설명|
|-section|section으로 구분해서 매뉴얼을 찾아 보여준다.|

각 세션의 편성

- 1절 - Commands(명령어)

- 2절 - System Calls(시스템 호출)

- 3절 - Subroutines(라이브러리 함수)

- 4절 - Special files(특수 파일)

- 5절 - File formats and conventions(파일형식)

- 6절 - Games(게임)

- 7절 - Macro package and language conventions(기타 정보)

- 8절 - Maintenance commands and procedures(보수)

### 2. 페이지 단위 파일 출력(more or less)
파일의 내용을 페이지 단위로 보여준다.

|일반 형식| less file_name|
|------|------|
|명령|설명.|
|스페이스 바, f|한 번에 한 페이지씩 전방으로 스크롤한다.|
|리턴|한 번에 한 줄씩 전방으로 스크롤한다.|
|b|한 번에 한 페이지씩 역방향으로 스크롤한다.|
|q|프로그램을 종료한다.|
|/문자열|문자열을 검색한다.|

### 3. 사용자의 권한

![image](https://user-images.githubusercontent.com/73567433/125375786-a10cd500-e3c4-11eb-8d90-4ce2170498ed.png)

![image](https://user-images.githubusercontent.com/73567433/125375807-a8cc7980-e3c4-11eb-8329-57991e913af8.png)

chmod : 파일의 모드를 바꾸어 권한을 제어할 수 있도록 한다.
chown : 파일의 소유자를 변경한다.
chgrp : 파일의 그룹을 변경시킨다.

|일반 형식| chmod ［-cfvR］모드 파일명(들)|
|------|------|
|옵션|설명|
|-c|실제로 파일의 권한이 바뀐 파일만 자세히 기술한다.|
|-f|파일의 권한이 바뀔 수 없어도 에러 메시지를 출력하지 않는다.|
|-v|변경된 권한에 대해서 자세히 기술한다.|
|-R|디렉터리와 파일들의 권한을 재귀적으로 모두 바꾼다.|

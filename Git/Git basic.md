# **Git Basic**
- **버전**: sw특정상태
- **버전관리** : 변경사항 분석
- **git ->분산버전관리프로그램**
- **github** -> git기반의 저장소 제공 서비스업체
- **분산버전관리** : not 중앙집중식(한곳에모여관리) / 
- git 베이스 서버 : 싸피 -> git lab , github
- **TIL** : Today I learned
---
- git hub repository -> toy project 그룹
- git 적어도 일주일에 3~4번 commit
---
- **GUI (graphic user interface)**: 그래픽을 통해 사용자와 컴터가 상호작용 (클릭해서 폴더이동) -> 사용하기쉽지만 성능 더많이 소모
- **CLI (command user interface)**: 명령어를 통해 '' -> 수많은 서버/개발시스템이 이를이용
---
## CLI폴더

1. 바탕화면에 **cli폴더**만들고 우클릭 **git bash here**
2. **touch 파일명**: 파일(not folder)을 생성하는 명령어
3. **ls** : 현재작업중인 폴더/파일 목록
4. **mkdir 폴더명**: 폴더 생성
5. **cd 폴더명**: 폴더내부로 이동 <path 정보 확인 중요!!!!>
6. **cd ..** : 폴더 밖으로 이동
7. **start 파일명**: 파일 열기 (메모장)
8. **code 파일명**: vs code로 파일 열기 (only vs code 설치시 사용가능)
9. **rm 파일명** : 파일(not folder)을 삭제
10. **rm -rf 폴더명** :폴더를 삭제
---
- **절대경로**: 루트 DIR부터 목적지점까지 모든경로  (C:/Users/ssafy/Desktop)
- **상대경로**: 현재 작업중인 DIR 기준 계산된 상대적 위치 (~/Desktop/cli)
-> ./ : 현재작업중폴더,  ../ : 현재작업 상위폴더

- ex) Users에서 Desktop으로 이동
cd ./ssafy/Desktop
- ***README.md 의 url도 상대경로 이용***

---

## Markdown
- Markdown: 텍스트기반 마크업 언어, 문서구조와 내용을 쉽고빠르게 <typora> ->이용해서 github 정리

    - 헤딩
    - 리스트
    - 코드블럭

### **Typora**
```
[Typora]
1. # : 제목
2. - : ●
3. ** **: 굵게 (ctrl+b)
4. == ==: 색강조
5. > : 인용문
6. 1. : 순서가 있는 리스트
7. - [ ] : 체크박스
8. ```python 엔터 :
9. ctrl+t : 표삽입
10. --- 엔터: 가로줄 생성
11. [링크이름](url): 링크삽입
12. ![](): 이미지삽입
13. * *: 기울이기
14. ~~ ~~: 취소선
15. html 문법도 사용가능!
```
### **Notion**
```
[Notion]
-노션에서는 마크다운 문법이 살짝 다름
1. > : 토글 (not 인용문)
2. " : 인용문
3. /callout 엔터: 네모칸
4. /table: 표삽입
5. / 데이터베이스인라인 선택: 창이열리는 표
6. 노션 꾸밀때 indify사용!! (typora, markdown cheatsheet 참고)
```
---

# Github
- **README.md** <대문자로작성>: 프로젝트에 대한 설명 문서   
  - 오픈소스의 공식문서 작성 (개인프로젝트의 소개문서로 이용할 예정!!)
  - 작성형식은 따로없음, 제공받은 템플릿이용 
- *매일학습한 내용 정리할때 **markdown** 이용!*
- **Repository** : 특정 디렉토리(폴더)를 버전 관리하는 저장소 (repo)
- **local 환경**: 지금 사용중인 컴퓨터
---

## cli 폴더내에서 git bash
- **git init** -> **.git 폴더** 생성 (버전관리에 필요한 정보) , local저장소생성
- **ls -a** -> .git 숨겨진 폴더 보임 and branch가 **master**로 변경
---

## [Git 기본기]
1. **working directory**
2. **staging area**
3. **repository**
   - 세가지 영역을 바탕으로 local환경에서 동작
   - **wd** :내가 작업하고있는 실제 디렉토리 
   - **stg** :중간 확인공간, 커밋으로 버전관리할 대상 파일 
   - **repo** :버전관리가 저장되는 곳


>- 새롭게 추가된 상태인 untracked file (wd)
> 
>- "git add" -> staged (stg) -> "git commit" -> committed (repo)
> 
>- 수정되는경우 modified (wd) -> "git add" -> staged (stg) -> "git commit" -> committed (repo)   (변경사항들이 남아 축적됨)
>- git status :현재 상태 / git add . : 모든파일을 staging area로 이동 
---

## **Git 계정 등록**
```python
multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/cli (master)
$ git config --global user.email "k101613@gmail.com"

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/cli (master)
$ git config --global user.name "NayeonS2"

multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/cli (master)
$ git config --global --list
user.email=k101613@gmail.com
user.name=NayeonS2
```

>- 여기서 git commit하면 vim 창열림
>- [vim 2가지 mode]
>   1. command*  -> i키누르면 edit모드로 변경가능
>   2. edit -> esc누르면 나가기
:wq 엔터 : 저장하고 나가기
--> repo에 올려진것 (commit됨) -> git log 누르면 변경사항 확인가능


.md 파일 수정후 git status -> git add . -> git status -> git commit -m "modified 개발자로 성장하기"
-> git status and git log (위에께 최신수정)

git log --oneline
git diff hash1 hash2


remote repository : github
Github가서 create new repository
remote repository의 위치를 알려줘야함
git remote add [repo 별명] [repo 주소] 
-> git remote add origin https://github.com/NayeonS2/test.git
git remote -v (등록된 remote 정보 확인)
git push origin master (업데이트)

github 들어가서 overview에서 commits확인

[git으로 파일 내려받기]
ex) cli :강의장, startcamp:집
a.txt에 글작성, README 대문자로

git clone https://github.com/NayeonS2/test.git ---> local로 복제, .git 같이 복제, (remote주소도 같이복제) -> git init, git remote add ~ 할필요 ㄴㄴ
git add (master아니라서 안됨)
cd test
git add . -> git commit -m "modified a.text"


맨날 해햐하는것!!!!!
***************************************************
<강의장> -> "git pull origin master"
집에서공부한것 -> 강의장 : git pull origin master
add
push
강의장에서한거 push

<집> -> "git push origin master"
pull
공부
add
commit
push


*Clone vs. Push
-clone : local로 복제, .git 같이 복제, (remote주소도 같이복제) -> git init, git remote add ~ 할필요 ㄴㄴ
git add (master아니라서 안됨)
-push : remote 정보가 필요, 동일 버전으로 다운받는 것, 이미 git 관리 필요 (.git 폴더가 존재해야함)
git init
git remote
git pull



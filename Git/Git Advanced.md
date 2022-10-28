# Git Advanced

## Undoing (되돌리기)

## Working Directory 작업 단계 되돌리기
### git restore
- Working Directory에서 수정한 파일을 수정전(직전 커밋)으로 되돌리기
- 이미 버전관리가 되고있는 파일만 되돌리기 가능
- **git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의!**
- `git restore {파일 이름}`


 > [참고] stash (임시 보관)
  - `git stash`
  - `git stash apply` (임시 보관해놓은거 되돌리기)


## Staging Area 작업 단계 되돌리기
- staging area는 임시 목록
- git add를 잘못한 경우
- Staging Area에 반영된 파일을 Working Directory로 되돌리기 (==Unstage)
- root-commit이 없는 경우 : `git rm --cached`
  - 해당 파일을 한번이라도 commit 한 적이 없을때 (new file)
- root-commit이 있는 경우 : `git restore --staged `

### git rm --cached
- to unstage and remove paths only from the staging area
- **한번도 커밋을 안 한 경우**
- `git rm --cached {파일이름}`
- git add 한 이후에 git rm --cached하면 다시 staging area에서 내려와서 **Untracked** 됨!

### git restore --staged
- the contents are restored from **HEAD**
- **커밋을 한번이라도 한 경우**
- `git restore --staged {파일이름}`
- git add 한 이후에 git restore --staged하면 다시 staging area에서 내려와서 **Untracked** 됨!

## Repository 작업 단계 되돌리기
- 커밋을 수정한다
- 커밋을 완료한 파일을 Staging Area로 되돌리기
- `git commit --amend`
  - Staging Area에 새로 올라온 내용이 없다면, `직전 커밋의 메세지만 수정`
  - Staging Area에 새로 올라온 내용이 있다면, `직전 커밋을 덮어쓰기`
- **이전 커밋을 완전히 고쳐서 새 커밋으로 변경하므로,**
- **이전 커밋은 일어나지 않은 일이 되며 히스토리에도 남지 않음을 주의!**
- hash가 바뀌므로, 팀작업 시에는 되도록 amend사용 지양


> [참고] Vim
- 입력모드 `i`
- 명령모드 `esc`
  - 저장 및 종료 : `:wq`
  - 강제 종료 : `:q!` 

---
## Git reset & revert
- 특정 시간으로 되돌리기

### git reset
- 프로젝트를 특정 커밋(버전) 상태로 되돌림
- 특정 커밋으로 되돌아 갔을때, 해당 커밋 이후로 쌓였던 커밋들은 전부 사라짐
- `git reset [옵션] {커밋 ID}`
  - 옵션은 **soft, mixed, hard** 중 하나를 작성
  - 커밋 ID (oneline으로 했을때 hash 값)는 되돌아가고 싶은 시점의 커밋 ID를 작성

### git reset 세가지 옵션
- `--soft`
  - 해당 커밋으로 되돌아가고
  - **되돌아간 커밋 이후의 파일들은 Staging Area로 돌려놓음**
- `--mixed`
  - **되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음**
  - git reset옵션의 **기본값**
- `--hard`
  - **되돌아간 커밋 이후의 파일들은 Working Directory에서 삭제**
    - 사용시 주의! (복구는 가능)
      - git reflog
  - 기존 Untracked 파일은 사라지지 않고 Untracked로 남아있음

> [참고] git reflog
- git reflog 명령어를 이용하면 reset하기 전의 과거 커밋 내역을 모두 조회 가능
- 이후 커밋ID 복사해서 해당 커밋으로 reset 하면 hard 옵션으로 삭제된 파일도 복구 가능

### git revert
- **해당 커밋'을' 되돌리는 것**
  - **해당 커밋을 취소**시키고, **취소된 것을 기록으로 남기는것**
  - **git reset**은 **해당 커밋'으로' 되돌리는 것**
- 과거를 없었던 일로 만드는 행위, 이전 커밋을 취소한다는 새로운 커밋을 생성함
- git revert {커밋ID}
  - 커밋 ID는 취소하고 싶은 커밋 ID를 작성
- reset은 커밋 내역을 삭제하는 반면, revert는 새로운 커밋을 생성함
  

---

## Git branch

### git branch
- 브랜치는 나뭇가지라는 뜻으로, 여러갈래로 **작업공간을 나누어 독립적으로 작업**할 수 있도록 돕는 git 도구

- 장점
  - 브랜치는 독립 공간 형성하기때문에 원본(master)에 대해 안전
  - 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발 가능
  - git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

- **조회**
  - `git branch`
    - 로컬 저장소의 브랜치 목록 확인
  - `git branch -r`
    - 원격 저장소의 브랜치 목록 확인

- **생성**
  - `git branch {브랜치 이름}`
    - 새로운 브랜치 생성
  - `git branch {브랜치 이름} {커밋 ID}`
    - 특정 커밋 기준으로 브랜치 생성

- **삭제**
  - `git branch -d {브랜치 이름}`
    - merge된 브랜치만 삭제 가능
  - `git branch -D {브랜치 이름}`
    - 강제 삭제

- 권장 개발 과정 
  - 기능 개발 완료
  - merge Ok
  - branch 삭제

### git switch
- 현재 브랜치에서 다른 브랜치로 이동하는 명령어
-` git switch {브랜치 이름}`
  - 다른 브랜치로 이동
- `git switch -c {브랜치 이름}`
  - 브랜치를 새로 생성 및 이동
- `git switch -c {브랜치 이름} {커밋ID}`
  - 특정 커밋 기준으로 브랜치 생성 및 이동
- **switch하기 전에, 해당 브랜치의 변경사항을 반드시 커밋해야함을 주의!**

### HEAD
- HEAD는 현재 브랜치의 최신 커밋
- `git log --oneline`



---

## Git merge

- 분기된 브랜치들을 하나로 합치는 명령어
- mastser 브랜치가 상용이므로, 주로 master브랜치에 병합
- `git merge {합칠 브랜치 이름}`
  - master 선택된 상태에서
  - 병합하기 전에 브랜치를 합치려고 하는, 메인 브랜치로 switch해야함
  - 병합에는 세종류 존재
    - `Fast-Forward`
    - `3-way Merge`
    - `Merge Conflict`
- **merge한 이후엔 브랜치 삭제!!!**

### Fast-Forward
- 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법


### 3-way Merge
- 각 브랜치의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 방법

### Merge Conflict
- 두 브랜치에서 같은 부분을 수정한 경우
- git이 어느 브랜치의 내용으로 작성해야하는지 판단을 못해서 충돌이 발생했을때 이를 해결하며 병합하는 방법
- 보통 같은 파일의 같은 부분을 수정했을때 자주 발생함
- conflict 해결후
- add .
- commit 
- 해결!
- merge한 이후엔 브랜치 삭제

---


- Branch와 원격 저장소를 이용해 협업을 하는 두가지 방법
  - 원격 저장소 소유권이 있는 경우 
  - 원격 저장소 소유권이 없는 경우

### Shared repository model
- 원격 저장소가 자신의 소유이거나 **Collaborator**로 등록되어 있는 경우
- master 브랜치에 직접 개발하는 것이 아니라, 기능별로 **브랜치를 따로 만들어 개발**
- `Pull request`를 사용하여 팀원 간 변경 내용에 대한 소통 진행
- 1. clone 받기
- 2. 각자 branch 생성 후 기능개발
- 3. 기능 구현 완료되면, 본인 branch에 Push
- 4. Pull request를 통해 branch를 master에 반영해달라는 요청을 보냄
- 5. 병합이 완료된 브랜치는 불필요하므로 원격 저장소에서 삭제
- 6. master로 브랜치 변경
- 7. 병합이 완료된 master를 로컬에 Pull
- 8. 원격 저장소 master의 내용을 받았으므로, 기존 로컬 브랜치 삭제


### Fork & Pull
- 오픈소스 프로젝트 같이, 자신 소유가 아닌 원격 저장소인 경우
- 원본 원격 저장소를 내 원격 저장소에 그대로 복제 (Fork)
- 기능 완성 후 복제한 내 원격 저장소에 Push
- 이후 `Pull Request`를 통해 원본 원격 저장소에 반영될 수 있도록 요청함

- 1. 소유권 없는 원격 저장소를 fork
- 2. 내용을 clone
- 3. git remote add upstream [원본 URL]
- 4. 기능개발 완료후 내 원격 저장소에 해당 브랜치를 push
- 5. Pull request를 통해 upstream 에 반영요청
- 6. 좋은 코드라면 merge
- 7. 병합된 정보 pull
- 8. 브랜치 지우기



### git flow
- 5개의 브랜치로 나누어 소스코드 관리
  - master
    - 제품으로 출시가능한 브랜치
  - develop
    - 다음 출시 버전을 개발하는 브랜치
  - feature
    - 기능을 개발하는 브랜치
  - release
    - 이번 출시 버전을 준비하는 브랜치
  - hotfix
    - 출시 버전에서 발생한 버그를 수정하는 브랜치



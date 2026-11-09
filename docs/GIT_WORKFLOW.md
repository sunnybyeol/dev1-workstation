# Git 제출 절차

이 프로젝트 파일은 과정을 수행하고, 결과를 증명하는 파일입니다.

## 1. 저장소 생성과 첫 push

GitHub에서 공개 저장소 `dev1-workstation`을 생성. README와 .gitignore를 GitHub에서 미리 만들지 않도록 설정한 뒤 PowerShell에서 실행.

```powershell
Set-Location C:\dev\dev1-workstation
git init -b main
git config user.name "sunnybyeol"
git config user.email "witch_jh@naver.com"
git add README.md .gitignore main.py quiz_game.py storage.py state.json docs
git commit -m "chore: create Python quiz project"
git remote add origin https://github.com/sunnybyeol/dev1-workstation.git
git push -u origin main
```


## 2. 최소 10개의 의미 있는 커밋

1. `feat: add quiz and game models` — 모델 검증/직렬화 개선
2. `feat: add quiz menu` — 메뉴 흐름 개선
3. `feat: validate user input` — 숫자/빈 입력 처리 개선
4. `feat: add quiz creation flow` — 문제 등록 개선
5. `feat: persist quiz state` — 저장 구조 개선
6. `fix: recover from invalid state file` — 손상 파일 복구 개선
7. `feat: track best score` — 점수 기록 개선
8. `docs: explain quiz data format` — README 데이터 설명 개선
9. `docs: add usage screenshots` — 실제 캡처 추가
10. `docs: record Git workflow evidence` — 실제 브랜치/원격 작업 기록 추가

실제 커밋 수는 `git rev-list --count HEAD`로 확인.

## 3. 브랜치 생성과 병합

```powershell
git switch -c feature/quiz-help
# README에 실제 사용 예시나 도움말을 추가한 뒤 저장
git add README.md
git commit -m "docs: add quiz usage help"
git switch main
git merge --no-ff feature/quiz-help -m "merge: add quiz usage help"
git push
```

브랜치 목록과 그래프를 기록.

```powershell
git branch -a
git log --oneline --graph --decorate --all
```

## 4. clone과 pull 실습

기존 저장소 바깥의 별도 폴더에서 실행.

```powershell
Set-Location C:\dev
git clone https://github.com/sunnybyeol/dev1-workstation.git dev1-workstation-clone
Set-Location C:\dev\dev1-workstation-clone
```

원본 저장소에서 작은 README 변경을 commit/push한 뒤, 복제 폴더에서 가져옴.

```powershell
git pull origin main
git log -1 --oneline
```

clone 경로, pull 전후 상태와 실제 출력, 브랜치 병합 그래프를 제출용 README 또는 `docs/`의 기록에 추가.

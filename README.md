
# Python Basics Quiz

## 1. 프로젝트 소개

터미널에서 Python 기초 객관식 문제를 풀고, 문제와 최고 점수를 `state.json`에 저장하는 작은 퀴즈 게임입니다. Python 문법뿐 아니라 클래스, 파일 입출력, 예외 처리, Git 기초를 직접 확인할 수 있도록 구성했습니다.

퀴즈 주제는 **Python 기초**로 정했습니다. 변수와 자료형, 리스트, 함수, 예외 처리, JSON처럼 과제의 학습 목표와 바로 연결되는 내용을 문제로 만들 수 있고, 사용자가 직접 문제를 추가할 수도 있습니다.

## 2. 실행 환경

- Python 3.10 이상
- Windows PowerShell, 터미널 또는 Linux 셸, vscode
- 외부 패키지 설치 없음 (Python 표준 라이브러리만 사용)

## 3. 실행 방법

PowerShell에서 이 저장소 폴더로 이동해 실행합니다.

```powershell
Set-Location C:\dev\dev1-workstation
py -X utf8 main.py
```

macOS/Linux에서는 다음과 같이 실행합니다.

```bash
cd /path/to/dev1-workstation
python -X utf8 main.py
```

첫 실행 때 `state.json`이 없으면 기본 퀴즈를 불러와 파일을 생성합니다. 종료 후 다시 실행해도 추가한 문제와 최고 점수가 유지됩니다.

## 4. 메뉴와 기능

1. **퀴즈 풀기**: 저장된 문제에 답하고 점수를 계산합니다.
2. **퀴즈 추가**: 질문, 선택지 네 개, 정답 번호를 입력해 저장합니다.
3. **퀴즈 목록**: 저장된 질문과 선택지를 확인합니다.
4. **점수 확인**: 최고 점수, 최근 점수, 문제 수를 확인합니다.
5. **종료**: 진행 상태를 저장하고 끝냅니다.

숫자가 필요한 곳에 문자를 넣거나 범위를 벗어난 숫자를 입력하면 안내 후 다시 입력받습니다. 빈 질문/선택지는 거절합니다. Ctrl+C 또는 입력 종료도 안전하게 처리합니다. `state.json`이 없으면 기본 문제로 시작하고, JSON이 깨졌다면 원본을 가능한 경우 별도 파일로 보관한 뒤 기본 문제로 복구합니다.

## 5. 코드 구조

```text
dev1-workstation/
├── main.py                  # 메뉴, 입력 검증, 게임 흐름
├── quiz_game.py             # Quiz / QuizGame 클래스와 게임 규칙
├── storage.py               # 기본 문제, JSON 읽기/저장/복구
├── state.json               # 문제와 최고 점수 (UTF-8 JSON)
├── README.md                # 프로젝트 설명과 사용법
├── .gitignore               # 캐시 등 불필요 파일 제외
└── docs/
    ├── GIT_WORKFLOW.md       # 브랜치, 커밋, clone/pull 제출 절차
    └── screenshots/
        └── README.md         # 실제 화면 캡처 체크리스트
```

### 클래스 역할

- `Quiz`: 질문, 선택지 네 개, 정답 번호 하나를 검증하고 표현합니다.
- `QuizGame`: 문제 목록과 점수를 관리하고, 새 문제 추가와 최고 점수 갱신을 수행합니다.

### 데이터 파일

`state.json`은 프로젝트 루트에 생성됩니다. `quizzes` 배열 안에 각 질문과 선택지, 정답 번호를 저장하고 `best_score`에 최고 점수를 저장합니다. 저장은 UTF-8로 하고 임시 파일을 쓴 뒤 교체해 중간 저장 중 데이터 손상 가능성을 줄였습니다.

## 6. Git 작업 기록



GitHub 저장소를 만들고 로컬 변경을 올린 뒤, 최소 10개의 의미 있는 커밋, 기능 브랜치 병합, 저장소 clone과 pull 과정을 수행해야 합니다. 실제 사용자 계정과 원격 저장소가 필요한 단계는 [docs/GIT_WORKFLOW.md](docs/GIT_WORKFLOW.md)의 순서에 적어 두었습니다. 커밋/푸시를 실행했다고 가장하지 않으며, GitHub 주소와 로그 증거는 실제 수행 후 여기에 추가합니다.

## 7. 제출 전에 남길 증거

- 메뉴, 퀴즈 풀이, 문제 추가, 문제 목록, 점수 화면 캡처: [docs/screenshots/README.md](docs/screenshots/README.md)
- 개발 환경과 Python 버전 확인 기록


- `git log --oneline --graph` 결과와 브랜치 병합 기록
- GitHub 저장소 링크 및 실제 push 기록

화면 캡처와 원격 저장소 기록은 실제 실행/업로드 후 추가해야 합니다.
(docs/screenshots/1connect.png)
(docs/screenshots/2version.png)
(docs/screenshots/3gitbranch.png)

##실행화면

#퀴즈 실행화면
[docs/srceenshots/menu.png](docs/screenshots/menu.png)
###퀴즈 풀기
[docs/screenshots/play.png](docs/screenshots/play.png), [docs/screenshots/play.png](docs/screenshot/play1.png)
###퀴즈 추가
[docs/screenshots/add-quiz.png](docs/screenshots/add-quiz.png)
###퀴즈 목록
[docs/screenshots/quiz-list.png](docs/screenshots/quiz-list.png)
###점수 확인
[docs/restart-persistencescreenshots/score.png](docs/screenshots/score.png)
###종료 후 재시작 점수 남아있는지 확인
[docs/screenshots/score.png](docs/screenshots/restart-persistence.png)
###종료
=======
# dev1-workstation
mission 2
>>>>>>> d1eceed3a8eea6021850d696acfd8255f6eddbdf

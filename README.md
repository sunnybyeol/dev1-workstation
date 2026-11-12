
# Python Basics Quiz

## 1. 프로젝트 소개

터미널에서 Python 기초 객관식 문제를 풀고, 문제와 최고 점수를 `state.json`에 저장하는 작은 퀴즈 게임입니다. Python 문법뿐 아니라 클래스, 파일 입출력, 예외 처리, Git 기초를 직접 확인할 수 있도록 구성했습니다.

퀴즈 주제는 **Python 기초**로 정했습니다. 변수와 자료형, 리스트, 함수, 예외 처리, JSON처럼 과제의 학습 목표와 바로 연결되는 내용을 문제로 만들 수 있고, 사용자가 직접 문제를 추가할 수도 있습니다.

## 2. 실행 환경

- Python 3.10 이상
- Windows PowerShell, 터미널 또는 Linux 셸, vscode
- 외부 패키지 설치 없음 (Python 표준 라이브러리만 사용)

```powershell
py --version
```

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
5. **퀴즈 삭제**: 번호로 문제를 선택해 삭제합니다. 삭제 목록에서 `0`을 입력하면 취소하며, 삭제 결과는 `state.json`에 저장됩니다.
6. **종료**: 진행 상태를 저장하고 끝냅니다.


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
    ├── WORK_LOG.md           # 실행·검증 증거 기록 안내
    └── screenshots/
        └── README.md         # 실제 화면 캡처 체크리스트
```

### 클래스 역할

- `Quiz`: 질문, 선택지 네 개, 정답 번호 하나를 검증하고 표현합니다.
- `QuizGame`: 문제 목록과 점수를 관리하고, 문제 추가·삭제와 최고 점수 갱신을 수행합니다.

### 데이터 파일

`state.json`은 프로젝트 루트에 생성됩니다. `quizzes` 배열 안에 각 질문과 선택지, 정답 번호를 저장하고 `best_score`에 최고 점수를 저장합니다. 문제를 추가하거나 삭제하면 변경 내용이 저장됩니다. 저장은 UTF-8로 하고 임시 파일을 쓴 뒤 교체해 중간 저장 중 데이터 손상 가능성을 줄였습니다.

## 6. 보너스 기능 현황

현재 구현한 보너스 기능은 **퀴즈 삭제**입니다. 5번 메뉴에서 삭제할 문제 번호를 선택하며, `0`을 입력하면 취소합니다. 삭제 결과는 `state.json`에 저장됩니다. 

## 7. 실행 화면과 증거

캡처 파일은 모두 [docs/screenshots/](docs/screenshots/)에 저장되어 있습니다.

- 메뉴: [menu.png](docs/screenshots/menu.png) 
- 퀴즈 풀이: [play.png](docs/screenshots/play.png)
- 퀴즈 추가: [add-quiz.png](docs/screenshots/add-quiz.png)
- 퀴즈 목록: [quiz-list.png](docs/screenshots/quiz-list.png)
- 점수 확인: [score.png](docs/screenshots/score.png)
- 문제 삭제 : [quiz-del.png](docs/screenshots/quiz-del.png)
- 재실행, 삭제된 문제 확인 : [restart-persistence.png](docs/screenshots/restart-persistence.png)
- 잘못된 입력: [quiz-error.png](docs/screenshots/quiz-error.png) 
- Git 브랜치/clone/pull: [branchlist.png](docs/screenshots/branchlist.png), [clone.png](docs/screenshots/clone.png), [clonelist.png](docs/screenshots/clonelist.png), [pull.png](docs/screenshots/pull.png)
- 개발 환경: [2version.png](docs/screenshots/2version.png)

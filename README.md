
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
├── logs/                    # 실제 실행 및 Git 명령 출력
│   ├── menu-run.txt          # 메뉴 출력
│   ├── restart-persistence.txt # 재실행 후 문제·점수 확인
│   ├── input-validation.txt  # 입력 오류와 EOF 확인
│   ├── recovery-choice.txt   # 백업 실패 시 선택 흐름 확인
│   ├── json-recovery.txt     # 손상 JSON 백업·복구 확인
│   └── git-evidence.txt      # 원격·커밋·브랜치·병합 출력
└── docs/
    ├── GIT_WORKFLOW.md       # 브랜치, 커밋, clone/pull 제출 절차
    ├── WORK_LOG.md           # 실행·검증 증거 기록 안내
    ├── 미션_목표_설명.hwp     # 과제 목표와 요구사항 설명
    └── screenshots/
        └── README.md         # 실제 화면 캡처 체크리스트
```

### 클래스 역할

- `Quiz`: 질문, 선택지 네 개, 정답 번호 하나를 검증하고 표현합니다.
- `QuizGame`: 문제 목록과 점수를 관리하고, 문제 추가·삭제와 최고 점수 갱신을 수행합니다.

클래스는 문제와 점수처럼 함께 유지해야 하는 상태 및 그 상태를 바꾸는 동작을 묶습니다. 메뉴 흐름과 입력 검증은 독립 함수로 두어 사용자 입력을 다루고, 게임 규칙은 `QuizGame`에 맡겼습니다.

### 주요 함수와 메서드

- `main.ask_number()`는 숫자 변환과 범위를 확인하고, `main.delete_quiz()`는 삭제 대상을 사용자에게 선택받습니다.
- `QuizGame.delete_quiz()`는 1부터 시작하는 번호를 확인해 목록에서 문제 하나를 제거하고, `QuizGame.add_quiz()`는 `Quiz`를 생성해 질문·선택지·정답을 검증한 뒤 추가합니다.
- `storage.load_game()`은 JSON을 읽고 손상 시 백업·기본 상태 복구를 처리합니다. `storage.save_game()`은 임시 파일을 쓴 다음 `replace()`로 상태 파일을 교체합니다.

### 데이터 파일

`state.json`은 프로젝트 루트에 생성됩니다. `quizzes` 배열 안에 각 질문과 선택지, 정답 번호를 저장하고 `best_score`에 최고 점수를 저장합니다. 문제를 추가하거나 삭제하면 변경 내용이 저장됩니다. 저장은 UTF-8로 하고 임시 파일을 쓴 뒤 교체해 중간 저장 중 데이터 손상 가능성을 줄였습니다.

JSON은 사람이 읽고 편집하기 쉽고 Python 표준 라이브러리만으로 처리할 수 있어 작은 학습용 데이터에 적합합니다. 현재 `DEFAULT_QUIZZES`의 기본 문제는 **8개**이며, 제출 상태 파일에는 문제 **10개**, 최고 점수 **10점**이 있습니다. 추가 데이터가 늘어나면 날짜, 주제 같은 메타데이터를 문제 항목에 추가할 수 있습니다.

임시 파일 교체는 쓰기 도중 끊겨도 기존 파일이 부분적으로 덮이는 위험을 낮춥니다. 파일 잠금은 구현하지 않았으므로 여러 프로그램이 동시에 저장하면 마지막 저장이 앞선 저장을 덮을 수 있습니다. 데이터가 커져 메모리에 한 번에 올리기 어려워지면 SQLite, 대용량 줄 단위 처리에는 NDJSON을 고려합니다.

## 6. 보너스 기능 현황

현재 구현한 보너스 기능은 **퀴즈 삭제**입니다. 5번 메뉴에서 삭제할 문제 번호를 선택하며, `0`을 입력하면 취소합니다. 삭제 결과는 `state.json`에 저장됩니다.

## 7. 실행 화면과 증거

캡처 파일은 모두 [docs/screenshots/](docs/screenshots/)에 저장되어 있습니다.

- 메뉴: [menu.png](docs/screenshots/menu.png)
- 퀴즈 풀이: [play.png](docs/screenshots/play.png)
- 퀴즈 추가: [add-quiz.png](docs/screenshots/add-quiz.png)
- 퀴즈 목록: [quiz-list.png](docs/screenshots/quiz-list.png)
- 점수 확인: [score.png](docs/screenshots/score.png)
- 문제 삭제: [quiz-del.png](docs/screenshots/quiz-del.png)
- 재실행 후 영속성: [restart-persistence.png](docs/screenshots/restart-persistence.png)
- 잘못된 입력: [quiz-error.png](docs/screenshots/quiz-error.png)
- Git 브랜치/clone/pull: [branchlist.png](docs/screenshots/branchlist.png), [clone.png](docs/screenshots/clone.png), [clonelist.png](docs/screenshots/clonelist.png), [pull.png](docs/screenshots/pull.png)
- 개발 환경: [2version.png](docs/screenshots/2version.png)

## 8. 입력 예외와 복구 안내

| 입력·상황 | 프로그램의 동작 예시 |
|---|---|
| 메뉴에 `abc`, 빈 문자열, 5000자 비숫자 문자열 또는 5000자리 숫자 입력 | 숫자 변환을 거부하고 `숫자를 입력해 주세요.`를 표시한 뒤 다시 입력받습니다. |
| 메뉴 범위 밖 `7` 입력 | `1부터 6 사이의 숫자를 입력해 주세요.`를 표시하고 다시 입력받습니다. |
| 문제 정답에 `0` 또는 `5` 입력 | `1부터 4 사이의 숫자를 입력해 주세요.`를 표시하고 다시 입력받습니다. |
| 문제나 선택지에 공백만 입력 | `빈칸은 사용할 수 없습니다. 다시 입력해 주세요.`를 표시합니다. |
| Ctrl+C 또는 입력 종료(EOF) | `입력이 종료되어 프로그램을 안전하게 닫습니다.`를 표시하고, 일반 상태에서는 종료 처리에서 저장합니다. |
| `state.json`이 잘못된 JSON | 백업에 성공하면 오류와 백업 경로를 안내하고 기본 문제로 시작합니다. 예: `state.json could not be read (...); starter quizzes were loaded. A copy was saved as state.corrupt-20261112-120000.json.` 백업 실패 시에는 초기화 또는 저장하지 않고 종료를 선택합니다. |

손상 파일을 읽지 못하면 `storage.load_game()`이 `state.corrupt-날짜-시간.json` 이름으로 원본 백업을 시도하고 기본 문제를 반환합니다. 백업에 성공하면 기본 상태로 계속 진행할 수 있으며, 손상 전 데이터는 경고에 표시된 백업 파일에서 복원할 수 있습니다. 백업 복사 자체가 실패하면 `The damaged file could not be copied.`와 함께 복구 방법을 선택하게 됩니다. `1`은 기본 문제로 `state.json`을 초기화하고, `2` 또는 Ctrl+C/EOF는 저장하지 않고 종료해 원본을 보존합니다. 두 선택의 저장 여부는 [recovery-choice.txt](logs/recovery-choice.txt)에, JSON 백업 절차는 [json-recovery.txt](logs/json-recovery.txt)에 기록했습니다.

`main.py`는 입력과 화면 출력을 담당하고, `storage.py`는 파일 읽기·쓰기를 담당합니다. `QuizGame`의 규칙 메서드는 화면 출력이나 파일 접근 없이 메모리 상태를 바꿉니다. `ask_number()`는 입력과 안내 출력을 맡고, 저장 같은 파일 부수 효과는 `save_game()` 호출 지점에 둡니다.

## 9. Git 및 제출 증거

공개 원격 저장소: [sunnybyeol/dev1-workstation](https://github.com/sunnybyeol/dev1-workstation). 기능 브랜치는 작업을 `main`과 분리해 검토하기 위해 사용합니다. 실제 브랜치 목록, 원격 주소, 커밋 수와 병합 그래프는 [logs/git-evidence.txt](logs/git-evidence.txt)에 기록합니다. 실행 출력은 [logs/](logs/)에 두고, 메뉴·삭제·재실행 화면은 [docs/screenshots/](docs/screenshots/)에 정리했습니다.

clone과 pull 실행 화면은 [clone.png](docs/screenshots/clone.png)와 [pull.png](docs/screenshots/pull.png)에 있습니다. 현재 브랜치와 병합 결과의 텍스트 증거는 `logs/git-evidence.txt`의 실제 명령 출력으로 확인할 수 있습니다.

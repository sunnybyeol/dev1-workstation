# 실행·제출 증거 안내

이 폴더의 캡처는 실제 PowerShell 실행 화면이며, 명령의 원문 출력은 프로젝트 루트의 `logs/`에 텍스트로 기록합니다.

| 평가 내용 | 증거 |
|---|---|
| 최신 메뉴와 입력 오류 | `screenshots/menu.png`, `screenshots/quiz-error.png`, `../logs/menu-run.txt`, `../logs/input-validation.txt` |
| 퀴즈 삭제와 재실행 유지 | `screenshots/quiz-del.png`, `screenshots/restart-persistence.png`, `../logs/restart-persistence.txt` |
| 추가·목록·점수 | `screenshots/add-quiz.png`, `screenshots/quiz-list.png`, `screenshots/score.png` |
| Git 원격, 커밋 수, 브랜치·병합 | `../logs/git-evidence.txt` |
| clone/pull | `screenshots/clone.png`, `screenshots/clonelist.png`, `screenshots/pull.png` |

로그에는 명령, 실행 시각(한국 시간), 목적, 실제 출력과 종료 코드를 기록합니다. 자격 증명이나 계정 이메일은 로그에 넣지 않습니다.

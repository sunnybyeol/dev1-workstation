"""터미널에서 실행하는 Python 기초 퀴즈 게임."""

from __future__ import annotations

from quiz_game import QuizGame
from storage import STATE_PATH, load_game, save_game


class ExitRequested(Exception):
    """사용자가 Ctrl+C 또는 입력 종료를 요청했을 때 사용합니다."""


def ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError) as error:
        print("\n입력이 종료되어 진행 상황을 저장하고 프로그램을 닫습니다.")
        raise ExitRequested from error


def ask_non_empty(prompt: str) -> str:
    while True:
        value = ask(prompt)
        if value:
            return value
        print("빈칸은 사용할 수 없습니다. 다시 입력해 주세요.")


def ask_number(prompt: str, minimum: int, maximum: int) -> int:
    while True:
        raw = ask(prompt)
        try:
            value = int(raw)
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue
        if minimum <= value <= maximum:
            return value
        print(f"{minimum}부터 {maximum} 사이의 숫자를 입력해 주세요.")


def show_menu() -> None:
    print("\n===== 파이썬 기초 퀴즈 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록 보기")
    print("4. 점수 확인")
    print("5. 퀴즈 삭제")
    print("6. 종료")


def play_quiz(game: QuizGame) -> None:
    if not game.quizzes:
        print("저장된 문제가 없습니다. 먼저 퀴즈를 추가해 주세요.")
        return

    score = 0
    print(f"\n총 {len(game.quizzes)}문제를 시작합니다.")
    for number, quiz in enumerate(game.quizzes, start=1):
        print(f"\n문제 {number}: {quiz.question}")
        for choice_number, choice in enumerate(quiz.choices, start=1):
            print(f"  {choice_number}. {choice}")
        answer = ask_number("정답 번호 (1-4): ", 1, 4)
        if answer == quiz.answer:
            print("정답입니다!")
            score += 1
        else:
            print(f"아쉽습니다. 정답은 {quiz.answer}번입니다.")

    is_record = game.record_score(score)
    print(f"\n결과: {len(game.quizzes)}문제 중 {score}문제 정답")
    if is_record:
        print("새로운 최고 점수입니다!")
    print(f"최고 점수: {game.best_score}")


def add_quiz(game: QuizGame) -> None:
    print("\n객관식 퀴즈를 추가합니다. 선택지는 네 개입니다.")
    question = ask_non_empty("문제: ")
    choices = [ask_non_empty(f"선택지 {number}: ") for number in range(1, 5)]
    answer = ask_number("정답 번호 (1-4): ", 1, 4)
    game.add_quiz(question, choices, answer)
    save_game(game)
    print("퀴즈를 추가하고 저장했습니다.")


def list_quizzes(game: QuizGame) -> None:
    if not game.quizzes:
        print("저장된 문제가 없습니다.")
        return
    print(f"\n등록된 퀴즈: {len(game.quizzes)}개")
    for number, quiz in enumerate(game.quizzes, start=1):
        print(f"{number}. {quiz.question}")
        for choice_number, choice in enumerate(quiz.choices, start=1):
            marker = " (정답)" if choice_number == quiz.answer else ""
            print(f"   {choice_number}. {choice}{marker}")


def delete_quiz(game: QuizGame) -> None:
    if not game.quizzes:
        print("삭제할 문제가 없습니다.")
        return

    print("\n삭제할 퀴즈를 선택하세요. 취소하려면 0을 입력하세요.")
    for number, quiz in enumerate(game.quizzes, start=1):
        print(f"{number}. {quiz.question}")

    selection = ask_number("삭제할 문제 번호: ", 0, len(game.quizzes))
    if selection == 0:
        print("삭제를 취소했습니다.")
        return

    removed = game.delete_quiz(selection)
    print(f"퀴즈를 삭제했습니다: {removed.question}")


def show_score(game: QuizGame) -> None:
    print(f"최고 점수: {game.best_score}")
    print(f"최근 점수: {game.last_score}")
    print(f"저장된 문제: {len(game.quizzes)}개")


def run() -> None:
    game, warning = load_game()
    if warning:
        print(warning)
    # 첫 실행에서도 state.json이 생성되도록 기본 상태를 저장합니다.
    save_game(game)

    actions = {
        1: lambda: play_quiz(game),
        2: lambda: add_quiz(game),
        3: lambda: list_quizzes(game),
        4: lambda: show_score(game),
        5: lambda: delete_quiz(game),
    }

    try:
        while True:
            show_menu()
            selection = ask_number("메뉴 선택 (1-6): ", 1, 6)
            if selection == 6:
                break
            actions[selection]()
            save_game(game)
    except ExitRequested:
        pass
    finally:
        try:
            save_game(game)
            print(f"진행 상황을 {STATE_PATH.name}에 저장했습니다.")
        except OSError as error:
            print(f"저장하지 못했습니다: {error}")

    print("게임을 종료합니다.")


if __name__ == "__main__":
    run()

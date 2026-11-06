"""UTF-8 JSON persistence for quiz questions and the high score."""

from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from quiz_game import Quiz, QuizGame


STATE_PATH = Path(__file__).resolve().parent / "state.json"

DEFAULT_QUIZZES = [
    Quiz("Python에서 함수를 정의할 때 사용하는 키워드는 무엇인가요?", ["func", "def", "function", "make"], 2),
    Quiz("len([3, 5, 7])의 결과는 무엇인가요?", ["2", "3", "5", "7"], 2),
    Quiz("Python의 참 값을 나타내는 값은 무엇인가요?", ["true", "TRUE", "True", "1True"], 3),
    Quiz("Python 리스트의 첫 번째 인덱스는 무엇인가요?", ["-1", "0", "1", "인덱스가 없습니다"], 2),
    Quiz("키와 값의 쌍을 저장하는 기본 자료형은 무엇인가요?", ["list", "tuple", "dict", "set"], 3),
    Quiz("range(3)이 만드는 값은 무엇인가요?", ["1, 2, 3", "0, 1, 2", "0, 1, 2, 3", "3"], 2),
    Quiz("예외를 처리할 때 사용하는 키워드는 무엇인가요?", ["catch", "except", "error", "finally"], 2),
    Quiz("이 프로그램이 진행 정보를 저장하는 파일 형식은 무엇인가요?", ["CSV", "XML", "JSON", "HTML"], 3),
]


def default_game() -> QuizGame:
    return QuizGame(quizzes=list(DEFAULT_QUIZZES), best_score=0)


def load_game(path: Path = STATE_PATH) -> tuple[QuizGame, str | None]:
    """Load state, or recover safely with starter quizzes if it is missing/bad."""
    if not path.exists():
        return default_game(), "state.json was not found; starter quizzes were loaded."

    try:
        data: Any = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict) or not isinstance(data.get("quizzes"), list):
            raise ValueError("The root must contain a quizzes list.")
        return QuizGame.from_dict(data), None
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        backup_path = path.with_name(
            f"{path.stem}.corrupt-{datetime.now():%Y%m%d-%H%M%S}{path.suffix}"
        )
        try:
            shutil.copy2(path, backup_path)
            backup_note = f" A copy was saved as {backup_path.name}."
        except OSError:
            backup_note = " The damaged file could not be copied."
        warning = f"state.json could not be read ({error}); starter quizzes were loaded.{backup_note}"
        return default_game(), warning


def save_game(game: QuizGame, path: Path = STATE_PATH) -> None:
    """Write JSON atomically so an interrupted save is less likely to corrupt data."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = path.with_suffix(path.suffix + ".tmp")
    temporary_path.write_text(
        json.dumps(game.to_dict(), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    temporary_path.replace(path)



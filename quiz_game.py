"""Quiz domain model and in-memory game rules."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Quiz:
    """One multiple-choice question. Answers use 1-based option numbers."""

    question: str
    choices: list[str]
    answer: int

    def __post_init__(self) -> None:
        if not self.question.strip():
            raise ValueError("Question cannot be empty.")
        if len(self.choices) != 4:
            raise ValueError("A quiz must have exactly four choices.")
        if any(not choice.strip() for choice in self.choices):
            raise ValueError("Choices cannot be empty.")
        if not 1 <= self.answer <= 4:
            raise ValueError("Answer must be a number from 1 to 4.")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Quiz":
        return cls(
            question=str(data["question"]),
            choices=[str(choice) for choice in data["choices"]],
            answer=int(data["answer"]),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


class QuizGame:
    """Own the quiz collection and the saved high score."""

    def __init__(self, quizzes: list[Quiz], best_score: int = 0) -> None:
        if best_score < 0:
            raise ValueError("Best score cannot be negative.")
        self.quizzes = quizzes
        self.best_score = best_score
        self.last_score = 0

    def add_quiz(self, question: str, choices: list[str], answer: int) -> None:
        self.quizzes.append(Quiz(question, choices, answer))

    def delete_quiz(self, number: int) -> Quiz:
        """Delete and return a quiz using its 1-based position in the list."""
        if isinstance(number, bool) or not isinstance(number, int):
            raise ValueError("Quiz number must be an integer.")
        if not 1 <= number <= len(self.quizzes):
            raise ValueError("Quiz number is outside the available range.")
        return self.quizzes.pop(number - 1)

    def record_score(self, score: int) -> bool:
        """Save a new high score and return whether it is a record."""
        self.last_score = score
        if score > self.best_score:
            self.best_score = score
            return True
        return False

    def to_dict(self) -> dict[str, Any]:
        return {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "QuizGame":
        quizzes = [Quiz.from_dict(item) for item in data["quizzes"]]
        best_score = data.get("best_score", 0)
        if isinstance(best_score, bool) or not isinstance(best_score, int):
            raise ValueError("best_score must be an integer.")
        return cls(quizzes=quizzes, best_score=best_score)

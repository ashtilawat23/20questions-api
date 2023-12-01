""" Data Validation Schema """
from pydantic import BaseModel


class Question(BaseModel):
    question: str
    word: str


class GameData(BaseModel):
    word: str
    questions: list
    guessed_correctly: bool
    additional_data: dict = {}  # Any additional data you want to store

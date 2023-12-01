""" Data Validation Schema """
from pydantic import BaseModel


class Question(BaseModel):
    question: str
    word: str

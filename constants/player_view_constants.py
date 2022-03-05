from enum import Enum


class Answer(Enum):
    """Possible answers for this prompt"""
    BACK = 0
    CREATE = 1
    UPDATE = 2
    DELETE = 3
    VIEW = 4
    REPORT = 5


answers_list = {
    Answer.BACK: "Back",
    Answer.CREATE: "Create a new player",
    Answer.UPDATE: "Update a player",
    Answer.DELETE: "Delete a player",
    Answer.VIEW: "View players",
    Answer.REPORT: "Players's reports"
}

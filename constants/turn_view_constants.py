from enum import Enum

class Answer(Enum):
  """Possible answers for this prompt"""
  BACK = 0
  CREATE = 1
  UPDATE = 2
  DELETE = 3
  VIEW = 4

answers_list = {
  Answer.BACK: "Back",
  Answer.CREATE: "Create a new turn",
  Answer.UPDATE: "Update a turn",
  Answer.DELETE: "Delete a turn",
  Answer.VIEW: "View turns"
}

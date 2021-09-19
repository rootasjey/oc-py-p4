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
  Answer.CREATE: "Create a new tournament",
  Answer.UPDATE: "Update a tournament",
  Answer.DELETE: "Delete a tournament",
  Answer.VIEW: "View tournaments"
}

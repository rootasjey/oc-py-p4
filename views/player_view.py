import inquirer
from pprint import pprint
from enum import Enum
from views.create_player_view import create_player_prompt

ANSWER_KEY = "answer"

class Answer(Enum):
  """Possible answers for this prompt"""
  BACK = 0
  CREATE = 1
  UPDATE = 2
  DELETE = 2

answers_list = {
  Answer.BACK: "Back",
  Answer.CREATE: "Create a new player",
  Answer.UPDATE: "Update a player",
  Answer.DELETE: "Delete a player"
}

def player_prompt():
  """Display player prompt"""
  continue_prompt = True

  while (continue_prompt):
    answer = main_question()

    if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
      continue_prompt = False

    elif (answer[ANSWER_KEY] == answers_list[Answer.CREATE]):
      create_player_prompt()

    elif (answer[ANSWER_KEY] == answers_list[Answer.UPDATE]):
      pprint("This feature is NOT yet available.")

    elif (answer[ANSWER_KEY] == answers_list[Answer.DELETE]):
      pprint("This feature is NOT yet available.")

    else:
      pprint("Something unexpected happened")

def main_question():
  """Display the main question to the user."""

  answer = inquirer.prompt([
      inquirer.List(
          ANSWER_KEY,
          message="Player: What do you want to do?",
          choices=[
            answers_list[Answer.CREATE], 
            answers_list[Answer.UPDATE], 
            answers_list[Answer.DELETE],
            answers_list[Answer.BACK],
          ],
      )
  ])

  return answer

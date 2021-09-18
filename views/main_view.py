import inquirer
from pprint import pprint
from enum import Enum
from views.player_view import player_prompt

ANSWER_KEY = "answer"

class Answer(Enum):
  """Possible answers for this prompt"""
  EXIT = 0
  PLAYER = 1
  TOURNAMENT = 2

answers_list = {
  Answer.EXIT: "Exit",
  Answer.PLAYER: "Manage players",
  Answer.TOURNAMENT: "Manage tournaments",
}

def prompt():
    """Show the main prompt."""
    continue_prompt = True

    while (continue_prompt):
      answer = main_question()

      if (answer[ANSWER_KEY] == answers_list[Answer.EXIT]):
        continue_prompt = False
      
      elif (answer[ANSWER_KEY] == answers_list[Answer.PLAYER]):
        player_prompt()

      elif (answer[ANSWER_KEY] == answers_list[Answer.TOURNAMENT]):
        pprint("This feature is NOT yet available.")
      else:
        pprint("Something unexpected happened")


def main_question():
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            ANSWER_KEY,
            message = "General: What do you want to do?",
            choices = [
              answers_list[Answer.PLAYER], 
              answers_list[Answer.TOURNAMENT], 
              answers_list[Answer.EXIT]
            ],
        )
    ])

    return answer

import inquirer
from enum import Enum
from controllers.player_controller import delete_player
from constants.common_constants import ANSWER_KEY
from constants.common_constants import SOMETHING_UNEXPECTED_STR
from views.player.create_player_view import create_player_prompt

class Answer(Enum):
    """Possible answers for this prompt"""
    UPDATE = 0
    DELETE = 1
    BACK = 2


answers_list = {
    Answer.UPDATE: "Update",
    Answer.DELETE: "Delete",
    Answer.BACK: "Back",
}


def single_player_prompt(player):
    """Show players in the console."""

    continue_prompt = True

    while (continue_prompt):
      answer = main_question(player)

      if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
        continue_prompt = False

      elif (answer[ANSWER_KEY] == answers_list[Answer.UPDATE]):
        create_player_prompt(player)

      elif (answer[ANSWER_KEY] == answers_list[Answer.DELETE]):
        delete_player(player)
        # return to previous prompt since this player is now deleted
        continue_prompt = False

      else:
        print(SOMETHING_UNEXPECTED_STR)


def main_question(player):
  """Display the main question to the user."""

  answer = inquirer.prompt([
      inquirer.List(
          ANSWER_KEY,
          message=f"{player.first_name} {player.last_name}: What do you want to do?",
          choices=[
            answers_list[Answer.UPDATE], 
            answers_list[Answer.DELETE],
            answers_list[Answer.BACK],
          ],
          carousel=True,
      )
  ])

  return answer


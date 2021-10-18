import inquirer
from enum import Enum
from controllers.tournament_controller import delete_tournament
from constants.common_constants import ANSWER_KEY
from constants.common_constants import SOMETHING_UNEXPECTED_STR, NOT_AVAILABLE_FEATURE_STR
from views.tournament.create_tournament_view import create_tournament_prompt
from views.tournament.add_player import add_player_tournament_prompt

class Answer(Enum):
    """Possible answers for this prompt"""
    ADD_TURN = 0
    ADD_PLAYER = 1
    UPDATE = 2
    DELETE = 3
    BACK = 4


answers_list = {
    Answer.ADD_TURN: "Add turn",
    Answer.ADD_PLAYER: "Add player",
    Answer.UPDATE: "Update",
    Answer.DELETE: "Delete",
    Answer.BACK: "Back",
}


def single_tournament_prompt(tournament):
    """Show tournaments in the console."""

    continue_prompt = True

    while (continue_prompt):
      answer = main_question(tournament)

      if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
        continue_prompt = False

      elif (answer[ANSWER_KEY] == answers_list[Answer.ADD_PLAYER]):
        add_player_tournament_prompt(tournament)

      elif (answer[ANSWER_KEY] == answers_list[Answer.ADD_TURN]):
        print(NOT_AVAILABLE_FEATURE_STR)

      elif (answer[ANSWER_KEY] == answers_list[Answer.UPDATE]):
        create_tournament_prompt(tournament)

      elif (answer[ANSWER_KEY] == answers_list[Answer.DELETE]):
        delete_tournament(tournament)
        # return to previous prompt since this tournament is now deleted
        continue_prompt = False

      else:
        print(SOMETHING_UNEXPECTED_STR)


def main_question(tournament):
  """Display the main question to the user."""

  answer = inquirer.prompt([
      inquirer.List(
          ANSWER_KEY,
          message=f"{tournament.name} {tournament.location} ({tournament.start_date}): What do you want to do?",
          choices=[
            answers_list[Answer.ADD_PLAYER], 
            answers_list[Answer.ADD_TURN], 
            answers_list[Answer.UPDATE], 
            answers_list[Answer.DELETE],
            answers_list[Answer.BACK],
          ],
          carousel=True,
      )
  ])

  return answer

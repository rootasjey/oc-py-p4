import inquirer
from enum import Enum
from constants.common_constants import ANSWER_KEY
from constants.common_constants import SOMETHING_UNEXPECTED_STR, NOT_AVAILABLE_FEATURE_STR
from controllers.turn_controller import get_all_turns_as_list, get_turn_from_id, deserialize_turn

class Answer(Enum):
    """Possible answers for this prompt"""
    ADD_EXISTING = 0
    CREATE_NEW = 1
    BACK = 2


answers_list = {
    Answer.ADD_EXISTING: "Add existing turn",
    Answer.CREATE_NEW: "Create new turn",
    Answer.BACK: "Back",
}


def add_turn_tournament_prompt(tournament):
    """Show tournaments in the console."""

    continue_prompt = True

    while (continue_prompt):
      answer = main_question(tournament)

      if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
        continue_prompt = False

      elif (answer[ANSWER_KEY] == answers_list[Answer.ADD_EXISTING]):
        show_existin_turns()

      elif (answer[ANSWER_KEY] == answers_list[Answer.CREATE_NEW]):
        print(NOT_AVAILABLE_FEATURE_STR)

      else:
        print(SOMETHING_UNEXPECTED_STR)


def main_question(tournament):
  """Display the main question to the user."""

  answer = inquirer.prompt([
      inquirer.List(
          ANSWER_KEY,
          message=f"{tournament.name} {tournament.location} ({tournament.start_date}): What do you want to do?",
          choices=[
            answers_list[Answer.ADD_EXISTING], 
            answers_list[Answer.CREATE_NEW], 
            answers_list[Answer.BACK],
          ],
          carousel=True,
      )
  ])

  return answer

def show_existin_turns():
  """Show a list of existing players to add to this tournament."""
  turns_list = get_all_turns_as_list()

  questions = [
      inquirer.Checkbox(
          ANSWER_KEY,
          message="Which turns do you want to add?",
          choices=turns_list,
          carousel=True,
      ),
  ]

  answers = inquirer.prompt(questions)

  if (answers[ANSWER_KEY] == answers_list[Answer.BACK]):
    print("nothing")
  else:
      turns_data = answers[ANSWER_KEY]
      print(turns_data)
      print('------')

      for turn_data in turns_data:
        turn =  get_turn_from_id(turn_data)
        turn = deserialize_turn(turn_data)
        show_single_turn(turn)
        


def show_single_turn(turn):
    """Format & display a single turn to the console."""
    
    print("------")
    print(
        f"• Name: {turn.name}\n• Start_date: {turn.start_date}\n• End_date: {turn.end_date}"
    )
    print("------")
    print("")
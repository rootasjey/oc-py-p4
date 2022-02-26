import inquirer
from enum import Enum
from constants.common_constants import ANSWER_KEY
from controllers.turn_controller import  get_turn_from_id
from views.turn.single_turn_view import single_turn_prompt


class Answer(Enum):
    """Possible answers for this prompt"""
    BACK =0


answers_list = {
  Answer.BACK: "Back",
}


def show_turns_tournament_prompt(tournament):
  """Show a list of existing turns in this tournament."""

  continue_prompt = True

  while continue_prompt:
    turn_ids_list=tournament.turns
    if len(turn_ids_list)!=0:
     
      turns_list = get_turns_names_from_ids(turn_ids_list)

      questions = [
        inquirer.List(
            ANSWER_KEY,
            message="list of turns added",
            choices=turns_list,
            carousel=True,
        ),
      ]
      answers = inquirer.prompt(questions)

      if (answers[ANSWER_KEY] == answers_list[Answer.BACK]):
        continue_prompt = False
      
      else:
      
        turn = get_turn_from_id(answers
        [ANSWER_KEY])
      
        show_single_turn(turn)
        single_turn_prompt(turn, tournament)
      return answers_list[Answer.BACK]
    else:
      print("Sorry no turn thanks to add a turn" )
      return answers_list[Answer.BACK]

  

def get_turns_names_from_ids(turn_ids = []):
  """Retrieve players names and elo from their id."""

  turns_list = []

  for turn_id in turn_ids:
    turn = get_turn_from_id(turn_id)
    turns_list.append((f"{turn.name}",f"{turn.id}"))
  print("######################")
  print(turns_list)
  return turns_list

  
  

def show_single_turn(turn):
    """Format & display a single turn to the console."""
    
    print("------")
    print(
        f"• Name: {turn.name}\n• Start time: {turn.start_time}\n• End time: {turn.end_time}"
    )
    print("------")
    print("")


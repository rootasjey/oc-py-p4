
import inquirer
from enum import Enum
from constants.common_constants import ANSWER_KEY
from controllers.turn_controller import get_all_turns_as_list,create_next_match

#from views.turn.generate_next_turn import generate_next_turn_prompt
from controllers.tournament_controller import add_turn_to_tournament

class Answer(Enum):
    """Possible answers for this prompt"""
    BACK = 0
    #CREATE_NEXT = 1



answers_list = {
    #Answer.CREATE_NEXT: "Create next  turn",
    Answer.BACK: "Back",
}


def add_turn_tournament_prompt(turn,tournament):
    """Show tournaments in the console."""

    continue_prompt = True

    while (continue_prompt):
      answer = main_question(tournament)

      if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
        continue_prompt = False

      else:  
        #(answer[ANSWER_KEY] == answers_list[Answer.CREATE_NEXT])
        #turn = generate_next_turn_prompt()
        add_turn_to_tournament(tournament, turn)
        #create_next_match(turn,tournament)
       


def main_question(tournament):
  """Display the main question to the user."""

  answer = inquirer.prompt([
      inquirer.List(
          ANSWER_KEY,
          message=": What do you want to do?",
          choices=[ 
            #answers_list[Answer.CREATE_NEXT],  
            answers_list[Answer.BACK],
          ],
          carousel=True,
      )
  ])

  return answer

def show_existing_turns(tournament):
  """Show a list of existing players to add to this tournament."""
  turns_list = get_all_turns_as_list(include_back=False)

  questions = [
      inquirer.Checkbox(
          ANSWER_KEY,
          message="Which turns do you want to add?",
          choices= turns_list,
      ),
  ]

  answers = inquirer.prompt(questions)
  turns_data = answers[ANSWER_KEY]
  return turns_data
  
  
def show_single_turn(turn):
    """Format & display a single turn to the console."""
    
    print("------")
    print(
        f"• Name: {turn.name}\n• Start_date: {turn.start_date}\n• End_date: {turn.end_date}"
    )
    print("------")
    print("")
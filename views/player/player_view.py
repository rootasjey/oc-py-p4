import inquirer
from pprint import pprint
from views.player.create_player_view import create_player_prompt
from views.player.show_player_view import show_player_prompt
from constants.player_view_constants import Answer, answers_list
from controllers.player_controller import sorted_players_by_alphab,sorted_players_by_elo
from models.player import Player
from constants.common_constants import ANSWER_KEY, SOMETHING_UNEXPECTED_STR

def player_prompt():
  """Display player prompt"""
  continue_prompt = True

  while (continue_prompt):
    answer = main_question()

    if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
      continue_prompt = False

    elif (answer[ANSWER_KEY] == answers_list[Answer.CREATE]):
      create_player_prompt()

    elif (answer[ANSWER_KEY] == answers_list[Answer.VIEW]):
      show_player_prompt()

    elif (answer[ANSWER_KEY] == answers_list[Answer.REPORT]):
        question = [
          inquirer.List(
          "type",
           message="What type of report?",
           choices=["Alphabet", "Elo"],
          ),
        ]
        
        answers = inquirer.prompt(question)
        if (answers['type']) == "Alphabet":
          sorted_players_by_alphab()
        elif (answers['type']) == "Elo":
          
          sorted_players_by_elo()
          

    else:
      pprint(SOMETHING_UNEXPECTED_STR)

def main_question():
  """Display the main question to the user."""

  answer = inquirer.prompt([
      inquirer.List(
          ANSWER_KEY,
          message="Player: What do you want to do?",
          choices=[
            answers_list[Answer.CREATE], 
            answers_list[Answer.VIEW],
            answers_list[Answer.REPORT],
            answers_list[Answer.BACK],
          ],
          carousel=True,
      )
  ])

  return answer

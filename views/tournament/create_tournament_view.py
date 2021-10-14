import inquirer
from enum import Enum
import datetime
from models.player import Player
from controllers.player_controller import save_player
import re


class Answer(Enum):
  """Possible answers for this prompt"""
  FIRST_NAME = 0
  LAST_NAME = 1
  BIRTH_DATE = 2
  SEX = 3
  ELO = 4

answers_list = {
  Answer.FIRST_NAME: "First name",
  Answer.LAST_NAME: "Last name",
  Answer.BIRTH_DATE: "Birth date",
  Answer.SEX: "Sex",
  Answer.ELO: "Elo",
}


def create_tournament_prompt():
  """Create a new player and add them to the database"""
  answers = start_questions()
  
  #date_string = answers[answers_list[Answer.BIRTH_DATE]]
  #check_birth_date(date_string)

  player = Player(
    first_name = answers[answers_list[Answer.FIRST_NAME]],
    last_name = answers[answers_list[Answer.LAST_NAME]],
    birth_date = answers[answers_list[Answer.BIRTH_DATE]],
    sex = answers[answers_list[Answer.SEX]],
    elo = answers[answers_list[Answer.ELO]],
  )

  save_player(player)


def start_questions():
  """Start a serie of question to create a new player."""
  answers = inquirer.prompt([
      inquirer.Text(
        answers_list[Answer.FIRST_NAME], 
        message = "What is your first name ?",
        default = "Rose",
        show_default = True,
      ),
      
      inquirer.Text(
        answers_list[Answer.LAST_NAME], 
        message = "What is your last name ?",
        default = "Quartz",
        show_default = True,
      ),

      inquirer.Text(
          answers_list[Answer.BIRTH_DATE],
          message = "What is your birth date ?",
          default = "02/01/90",
          show_default = True,
      ),

      inquirer.Text(
        answers_list[Answer.SEX], 
        message = "What is your gender ?",
        default = "",
        show_default = True
      ),

      inquirer.Text(
        answers_list[Answer.ELO], 
        message = "What is your rank ?",
        validate = lambda _, x: re.match("\d{1,4}", x),
        default = 600,
        show_default = True,
      ),
  ])
  
  return answers

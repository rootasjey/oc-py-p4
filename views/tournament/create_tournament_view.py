import inquirer
from enum import Enum
from models.tournament import Tournament
from controllers.tournament_controller import create_tournament,update_tournament

import re


class Answer(Enum):
  """Possible answers for this prompt"""
  NAME = 0
  LOCATION = 1
  START_DATE = 2
  END_DATE = 3
  TURNS = 4
  PLAYERS = 5
  TIME_CONTROL = 6
  DESCRIPTION = 7

answers_list = {
  Answer.NAME: "Name",
  Answer.LOCATION: "Location",
  Answer.START_DATE: "Start date",
  Answer.END_DATE: "End date",
  Answer.TURNS: "Number of turns",
  Answer.PLAYERS: "Players",
  Answer.TIME_CONTROL: "Time control",
  Answer.DESCRIPTION: "Description",
}


def create_tournament_prompt(tournament=None):
  """Create a new player and add them to the database"""
  answers = start_questions()
  
  #date_string = answers[answers_list[Answer.BIRTH_DATE]]
  #check_birth_date(date_string)

  new_tournament = Tournament(
    name = answers[answers_list[Answer.NAME]],
    location = answers[answers_list[Answer.LOCATION]],
    start_date = answers[answers_list[Answer.START_DATE]],
    end_date = answers[answers_list[Answer.END_DATE]],
    number_of_turns = answers[answers_list[Answer.TURNS]],
    turns = [],
    players = [],
    #players = answers[answers_list[Answer.PLAYERS]],
    time_control = answers[answers_list[Answer.TIME_CONTROL]],
    description = answers[answers_list[Answer.DESCRIPTION]],
  )

  #create_tournament(new_tournament)

  if tournament == None:
    new_tournament = create_tournament(new_tournament)
  else:
    new_tournament.id = tournament.id
    update_tournament(new_tournament)

  return new_tournament


def start_questions():
  """Start a serie of question to create a new tournament."""
  answers = inquirer.prompt([
      inquirer.Text(
        answers_list[Answer.NAME], 
        message = "What is your tournament name?",
        default = "Local tournament 1",
        show_default = True,
      ),
      
      inquirer.Text(
        answers_list[Answer.LOCATION], 
        message = "Where does this tournament takes place?",
        default = "Bordeaux",
        show_default = True,
      ),

      inquirer.Text(
          answers_list[Answer.START_DATE],
          message = "When does it start?",
          default = "10/28/21",
          show_default = True,
      ),

      inquirer.Text(
        answers_list[Answer.END_DATE], 
        message = "When does it end?",
        default = "10/30/21",
        show_default = True
      ),

      inquirer.Text(
        answers_list[Answer.TURNS], 
        message = "How many turns will it have?",
        validate = lambda _, x: re.match("\d{1,2}", x),
        default = 4,
        show_default = True,
      ),

      inquirer.Text(
        answers_list[Answer.TIME_CONTROL], 
        message = "How do we control time?",
        choices=['Blitz', 'Bulet', 'Rapid'],
      ),

      inquirer.Text(
        answers_list[Answer.DESCRIPTION], 
        message = "What is it description?",
        default = "An awesome tournament",
        show_default = True
      ),
  ])
  
  return answers

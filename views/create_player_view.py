import inquirer
from pprint import pprint
from enum import Enum
import datetime
from models.player import Player
from controllers.player_controller import save_player

# Constants to avoid manipulate strings value
# → reduce typo mistakes
ANSWER_KEY = "answer"

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

def create_player_prompt():
  """Create a new player and add them to the database"""
  answers = start_questions()
  
  date_string = answers[answers_list[Answer.BIRTH_DATE]]
  check_birth_date(date_string)

  player = Player(
    first_name = answers[answers_list[Answer.FIRST_NAME]],
    last_name = answers[answers_list[Answer.LAST_NAME]],
    birth_date = answers[answers_list[Answer.BIRTH_DATE]],
    sex = answers[answers_list[Answer.SEX]],
    elo = answers[answers_list[Answer.ELO]],
  )

  save_player(player)


def check_birth_date(birth_date = ""):
  """Check if the brithdate is in the right format."""
  
  try:
    datetime.datetime.strptime(birth_date, "%m/%d/%y")
    return True
  except ValueError as err:
    pprint(f"Sorry the date you provided {birth_date} (MM/DD/YY) → (Month/Day/Year) is not a valid date.")
    print(err)
    return False


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
          #validate = lambda _, x: re.match('\d{1,8}', x),
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
        message="What is your rank ?",
        default = "1200",
        show_default = True,
      ),
  ])
  
  return answers

import inquirer
import re
from pprint import pprint

def prompt():
    """Show the main prompt."""
    continue_prompt = True

    while (continue_prompt):
      answer = main_question()

      if (answer['answer'] == 'Exit'):
        continue_prompt = False
      elif (answer['answer'] == 'Manage players'):
        pprint("Manage players")
      elif (answer['answer'] == 'Manage tournaments'):
        pprint("Manage tournaments")
      else:
        pprint("Something unexpected happened")


def main_question():
    """Display the main question to the user."""

    answer = inquirer.prompt([
        inquirer.List(
            'answer',
            message="What do you want to do?",
            choices=['Manage players', 'Manage tournaments', 'Exit'],
        )
    ])

    return answer

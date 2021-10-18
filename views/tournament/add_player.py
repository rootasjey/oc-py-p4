import inquirer
from enum import Enum
from constants.common_constants import ANSWER_KEY
from constants.common_constants import SOMETHING_UNEXPECTED_STR, NOT_AVAILABLE_FEATURE_STR
from controllers.player_controller import get_all_players_as_list, get_player_from_id, deserialize_player
from controllers.tournament_controller import add_player_to_tournament

class Answer(Enum):
    """Possible answers for this prompt"""
    ADD_EXISTING = 0
    CREATE_NEW = 1
    BACK = 2


answers_list = {
    Answer.ADD_EXISTING: "Add existing player",
    Answer.CREATE_NEW: "Create new player",
    Answer.BACK: "Back",
}


def add_player_tournament_prompt(tournament):
    """Show tournaments in the console."""

    continue_prompt = True

    while (continue_prompt):
      answer = main_question(tournament)

      if (answer[ANSWER_KEY] == answers_list[Answer.BACK]):
        continue_prompt = False

      elif (answer[ANSWER_KEY] == answers_list[Answer.ADD_EXISTING]):
        show_existing_players(tournament)

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

def show_existing_players(tournament):
  """Show a list of existing players to add to this tournament."""
  players_list = get_all_players_as_list(include_back=False)

  questions = [
      inquirer.Checkbox(
          ANSWER_KEY,
          message="Which players do you want to add?",
          choices=players_list,
      ),
  ]

  answers = inquirer.prompt(questions)
  players_data = answers[ANSWER_KEY]

  for player_data in players_data:
    player_data =  get_player_from_id(player_data)
    player = deserialize_player(player_data)
    show_single_player(player)
    add_player_to_tournament(tournament, player)


def show_single_player(player):
    """Format & display a single player to the console."""
    
    print("------")
    print(
        f"• First name: {player.first_name}\n• Last name: {player.last_name}\n• Elo: {player.elo}\n• Sex: {player.sex}\n• Birth date: {player.birth_date}"
    )
    print("------")
    print("")
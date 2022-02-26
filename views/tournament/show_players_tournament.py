import inquirer
from enum import Enum
from constants.common_constants import ANSWER_KEY
from controllers.player_controller import  get_player_from_id
from views.player.single_player_view import single_player_prompt 
#from views.player.show_player_view  import show_player_prompt


class Answer(Enum):
    """Possible answers for this prompt"""
    BACK =0
  


answers_list = {
  Answer.BACK: "Back",
}


def show_players_tournament_prompt(tournament):
  """Show a list of existing players in this tournament."""
  
  continue_prompt = True
  
  while continue_prompt:
    player_ids_list=tournament.players
    if len(player_ids_list)!= 0:
      players_list = get_players_names_from_ids(player_ids_list)
    

      questions =[
        inquirer.List(
            ANSWER_KEY,
            message="list of players added",
            choices=players_list,
          carousel=True,
      
          
        ),
      ]

      answers = inquirer.prompt(questions)

      if (answers[ANSWER_KEY] == answers_list[Answer.BACK]):
        continue_prompt = False
      
      else :
      
        player = get_player_from_id(answers[ANSWER_KEY])
        show_single_player(player)
        single_player_prompt(player)
      return
    else :
      print("Sorry no player thanks to add " )
      return answers_list[Answer.BACK]

def get_players_names_from_ids(player_ids = []):
  """Retrieve players names and elo from their id."""

  players_list = []

  for player_id in player_ids:
    player = get_player_from_id(player_id)
    players_list.append((f"{player.name} {player.elo} ({player.sex}) {player.birth_date}", f"{player.id}"))

  return players_list
  

def show_single_player(player):
    """Format & display a single player to the console."""
    
    print("------")
    print(
        f"• First name: {player.first_name}\n• Last name: {player.last_name}\n• Elo: {player.elo}\n• Sex: {player.sex}\n• Birth date: {player.birth_date}"
    )
    print("------")
    print("")


import inquirer
from enum import Enum
from constants.common_constants import ANSWER_KEY

from controllers.player_controller import get_player_from_id
from views.match.single_match_view import single_match_prompt
from views.match.enter_score_player import enter_score_player_prompt

class Answer(Enum):
    """Possible answers for this prompt"""
    BACK =0


answers_list = {
  Answer.BACK: "Back",
}


def show_matchs_tournament_prompt(turn):
  """Show a list of existing turns in this tournament."""

  player_1_ids = []
  score_players_1 = []
  player_2_ids = []
  score_players_2 = []

  for player_id in turn.matchs:
    player_1 = (player_id[0][0])
    player_1_ids.append(player_1)
    player_2 = (player_id[1][0])
    player_2_ids.append(player_2)

    score_player_1 = player_id[0][1]
    score_players_1.append(score_player_1)
    
    score_player_2 = player_id[1][1]
    score_players_2.append(score_player_2)
  
  players_1 = []
  players_2 = []
  
  for player_1_id in player_1_ids:
    player_1 = get_player_from_id(player_1_id)
    players_1.append(player_1)

  for player_2_id in player_2_ids:
    player_2 = get_player_from_id(player_2_id)
    players_2.append(player_2)
  
  continue_prompt = True
  
  while continue_prompt:
  
    matchs_list = []
    index = 0

    for player in players_1:
      player_1 = players_1[index]
      score_1 = score_players_1[index]
      player_1_info = f"{player_1.name} (elo: {player_1.elo})(score : {score_1})"

      player_2 = players_2[index]
      score_2 = score_players_2[index]
      player_2_info = f"{player_2.name} (elo: {player_2.elo})(score : {score_2})"

      
      match = (f"Match : {player_1_info} <|> {player_2_info}", f"{index}")
      matchs_list.append(match)
      
      index = index + 1
    # adding back button
    matchs_list.append(answers_list[Answer.BACK])
    

    questions = [
      inquirer.List(
        ANSWER_KEY,
        message="list of matchs",
        choices=matchs_list,
        carousel=True,
      ),
    ]

    answers = inquirer.prompt(questions)

    if (answers[ANSWER_KEY] == answers_list[Answer.BACK]):
      continue_prompt = False
  
    else:
      print(answers)
      selected_match_index = int(answers['answer'])
     
      updated_match = enter_score_player_prompt(
        turn,
        selected_match_index,
        players_1[selected_match_index],
        players_2[selected_match_index],
      )

      if (updated_match):
        continue_prompt = False
      

      # 1. Extraire l'index du match sélectionné -> answers['answer']
      # 2. Appeler la méthode `single_match_prompt(...)` (autre fichier)
      #    avec en paramètre l'index du match sélectionné + tour (instance de classe),
      #    (et peut-être le tournoi mais pas sûr)
      # 3. Dans `single_match_promp(...)`, afficher un menu avec 'Back' et 'Update'
      # 4. Le bouton 'Update' demande à l'utilisateur d'entrer les scores 
      #    en premier lieu pour le joueur 1, puis pour le joueur 2
      # 5. Récupérer les valeurs saisies par l'utilisateur et créer un nouveau tuple
      #    avec les anciennes infos (les joueurs, index de match) + les scores mis à jour.
      # 6. Remplacer l'ancien tuple de match par le nouveau dans la liste (ou créer une nouvelle liste)
      # 7. Enregistrer cette nouvelle liste de matchs en base de données.
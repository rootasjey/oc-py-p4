from tinydb import TinyDB, where
from tinydb.table import Document
import uuid
from constants.player_view_constants import Answer, answers_list
from models.player import Player
import operator

db = TinyDB('data/players.json')

def delete_player(player):
  """Delete a single player from database."""
  db.remove(where('id') == player.id)

def deserialize_player(player_data):
  """From JSON data, return a Player instance object."""
  player =Player(
    player_data['id'], 
    player_data['first_name'], 
    player_data['last_name'], 
    player_data['birth_date'], 
    player_data['sex'], 
    player_data['elo'],
  )

  return player

def save_player(player):
  """Save a player to the database"""
  
  # Generate an unique identifier for a player.
  id = uuid.uuid4().int

  db.insert(
    Document({
      'id': id,
      'first_name': player.first_name,
      'last_name': player.last_name,
      'birth_date': player.birth_date,
      'sex': player.sex,
      'elo': int(player.elo),
    }, 
    doc_id = id)
  )

  print("")
  print("-------------")
  print(f"saved player: {player.name} ({player.elo})")
  print("-------------")
  print("")

  player.id = id
  return player

def update_player(player):
  """Update a player to the database"""

  db.update({
      'id': player.id,
      'first_name': player.first_name,
      'last_name': player.last_name,
      'birth_date': player.birth_date,
      'sex': player.sex,
      'elo': int(player.elo),
    }, 
    doc_ids = [player.id])

  print("")
  print("-------------")
  print(f"updated player: {player.name} ({player.elo})")
  print("-------------")
  print("")

def get_all_players():
  """Return all players from the database as a list of complexe data (Dictionnary of Dictionnary)"""
  return db.all()

def get_all_players_as_list(include_back = True):
  """Return all players from database as a list of string containing player's name and elo rating."""
  players = get_all_players()
  
  # Apply format_player() function to each player from database
  # and convert the result back (from an iterator) to a list.
  players_list = list(map(format_player, players))

  if include_back:
    # Append 'exit' entry at the end of the list.
    players_list.append(answers_list[Answer.BACK])

  return players_list

def get_player_from_id(player_id):
  """Return a player dictionnary from an id."""
  
  player_data = db.get(doc_id = int(player_id))
  return Player.fromJSON(player_data)



def format_player(player):
  """Format player output with name and elo."""
  
  player_id = f"{player['id']}" # to retrieve player data
  player_name = f"{player['first_name']} {player['last_name']} ({player['elo']})"
  return (player_name, player_id,)
def sorted_players_by_alphab():
  players = get_all_players_as_list() 
  sorted_list = sorted(players, key=lambda x: x[0])
  for player in sorted_list:
    print(f"{player[0]}")

def sorted_players_by_elo():
  players = get_all_players()
  
  sorted_list = sorted(players, key=lambda x: x['elo'], reverse=True)
  for player in sorted_list:
    print(f"{player['first_name']} {player['last_name']} ({player['elo']})")



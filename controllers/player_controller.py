from tinydb import TinyDB
from tinydb.table import Document
import uuid
from constants.show_player_view_constants import Answer, answers_list

db = TinyDB('data/players.json')

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

def get_all_players():
  """Return all players from the database as a list of complexe data (Dictionnary of Dictionnary)"""
  return db.all()

def get_all_players_as_list():
  """Return all players from database as a list of string containing player's name and elo rating."""
  players = get_all_players()
  
  # Apply format_player() function to each player from database
  # and convert the result back (from an iterator) to a list.
  players_list = list(map(format_player, players))

  # Append 'exit' entry at the end of the list.
  players_list.append(answers_list[Answer.BACK])

  return players_list

def get_player_from_id(player_id):
  """Return a player dictionnary from an id."""
  
  return db.get(doc_id = int(player_id))


def format_player(player):
  """Format player output with name and elo."""
  
  player_id = f"{player['id']}" # to retrieve player data
  player_name = f"{player['first_name']} {player['last_name']} ({player['elo']})"
  
  return (player_name, player_id)

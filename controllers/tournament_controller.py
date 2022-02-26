from tinydb import TinyDB, where
from tinydb.table import Document
import uuid
from constants.player_view_constants import Answer, answers_list
#from constants.tournament_view_constants import Answer, answers_list
from models.tournament import Tournament

db = TinyDB('data/tournaments.json') 

def add_turn_to_tournament(tournament,turn):
  """Add a new turn to the target tournament."""

  if turn.id not in tournament.turns:
    tournament.turns.append(turn.id)
    update_tournament(tournament)

    print(f"Successfully add turn '{turn.name}' to tournament {tournament.name} - {tournament.location} ({tournament.start_date} - {tournament.end_date})")

  else:
    print("Ce tour existe déjà dans le tournoi")

  print('_________')



 


def add_player_to_tournament(tournament, player):
  """Add a new player to the target tournament."""

  if player.id not in tournament.players:
    tournament.players.append(player.id)
    update_tournament(tournament)

    print(f"Successfully add player '{player.name}' to tournament {tournament.name} - {tournament.location} ({tournament.start_date} - {tournament.end_date})")

  else:
    print("Ce joueur existe déjà dans le tournoi")

  print('_________')



def update_tournament(tournament):
  """Save an existing tournament in database."""

  db.update({
    'id': tournament.id,
    'name': tournament.name,
    'location': tournament.location,
    'start_date': tournament.start_date,
    'end_date': tournament.end_date,
    'number_of_turns': tournament.number_of_turns,
    'turns': tournament.turns,
    'time_control': tournament.time_control,
    'players': tournament.players,
    'description': tournament.description,
    'encounters': tournament.encounters,
  }, 
  doc_ids = [tournament.id])

  

def delete_tournament(tournament):
  """Delete a single tournament from database."""
  db.remove(where('id') == tournament.id)

def deserialize_tournament(tournament_data):
  """From JSON data, return a tournament instance object."""

  tournament = Tournament(
    id=tournament_data['id'], 
    name=tournament_data['name'], 
    location=tournament_data['location'], 
    start_date=tournament_data['start_date'], 
    end_date=tournament_data['end_date'], 
    number_of_turns=int(tournament_data['number_of_turns']), 
    players=tournament_data['players'], 
    turns=tournament_data['turns'], 
    time_control=tournament_data['time_control'], 
    description=tournament_data['description'],
    encounters=tournament_data['encounters'],
  )

  return tournament

def create_tournament(tournament):
  """Save a new tournament to the database."""
  
  # Generate an unique identifier for a player.
  id = uuid.uuid4().int

  db.insert(
    Document({
      'id': id,
      'name': tournament.name,
      'location': tournament.location,
      'start_date': tournament.start_date,
      'end_date': tournament.end_date,
      'number_of_turns': tournament.number_of_turns,
      'turns': tournament.turns,
      'time_control': tournament.time_control,
      'players': tournament.players,
      'description': tournament.description,
      'encounters': tournament.encounters,
    }, 
    doc_id = id)
  )

  print("")
  print("-------------")
  print(f"saved tournament: {tournament.name} ({tournament.location})")
  print("-------------")
  print("")


def get_all_tournaments():
  """Return all tournaments from the database as a list of complexe data (Dictionnary of Dictionnary)"""
  return db.all()

def get_all_tournaments_as_list():
  """Return all tournaments from database as a list of string containing tournament's name and location."""
  tournaments = get_all_tournaments()
  
  # Apply format_tournament() function to each tournament from database
  # and convert the result back (from an iterator) to a list.
  tournaments_list = list(map(format_tournament, tournaments))

  # Append 'exit' entry at the end of the list.
  tournaments_list.append(answers_list[Answer.BACK])

  return tournaments_list

def get_tournament_from_id(tournament_id):
  """Return a tournament dictionnary from an id."""
  
  return db.get(doc_id = int(tournament_id))


def format_tournament(tournament):
  """Format tournament output with name and elo."""
  
  tournament_id = f"{tournament['id']}" # to retrieve tournament data
  tournament_name = f"{tournament['name']} {tournament['location']} ({tournament['start_date']})"
  
  return (tournament_name, tournament_id)

class Tournament:
  def __init__(self, id = None, name = '', location = '', 
                    start_date = 0, end_date = 0, number_of_turns = 4, 
                    list_turns = list, list_players = list, time_controle = '', description = ''):
    self.id = id
    self.name = name
    self.location = location
    self.start_date = start_date
    self.end_date= end_date
    self.number_of_turns = number_of_turns
    self.list_turns = list_turns
    self.list_players = list_players
    self.time_controle = time_controle
    self.description = description

  def __str__(self):
    return f"""{self.id} {self.name} {self.location} 
                {self.start_date} {self.start_date} {self.number_of_turns} 
                {self.list_turns} {self.list_players} {self.time_controle} {self.description}
    """
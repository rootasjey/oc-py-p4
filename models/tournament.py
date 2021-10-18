class Tournament:
  def __init__(self, id = None, name = '', location = '', 
                    start_date = 0, end_date = 0, number_of_turns = 4, 
                    turns = list, players = list, time_control = '', description = ''):
    self.id = id
    self.name = name
    self.location = location
    self.start_date = start_date
    self.end_date= end_date
    self.number_of_turns = number_of_turns
    self.turns = turns
    self.players = players
    self.time_control = time_control
    self.description = description

  def __str__(self):
    return f"""{self.id} {self.name} {self.location} 
                {self.start_date} {self.start_date} {self.number_of_turns} 
                {self.turns} {self.players} {self.time_control} {self.description}
    """
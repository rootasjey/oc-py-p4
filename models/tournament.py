# -*- coding: utf-8 -*-

from datetime import datetime



class Tournament:
  def __init__(self, id=None , 
                    name = '', 
                    location = '', 
                    start_date = 0, end_date = 0, number_of_turns = 4, 
                    turns = [],
                    players = [], time_control = '', description = '', encounters = {}):
    self.id = id
    self.name = name
    self.location = location
    self.start_date =  datetime.now().strftime("%d/%m/%Y")
    self.end_date= None
    self.number_of_turns = number_of_turns
    self.turns = turns
    self.players = players
    self.time_control = time_control
    self.description = description
    self.encounters = {}

  def __str__(self):
    return f"""{self.id} {self.name} {self.location} 
                {self.start_date} {self.start_date} {self.number_of_turns} 
                {self.turns} {self.players} {self.time_control} {self.description}
    """

 

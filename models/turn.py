# -*- coding: utf-8 -*-


class Turn:
    """
    Class representing a turn.
    """
    def __init__(self,id,name,start_time = "" ,end_time = "" ,matchs = []):
       
        self.id = id
        self.name = name
        self.matchs = matchs
        self.start_time = start_time
        self.end_time = end_time

    
    @staticmethod
    def fromJSON(json):
      """Create a new instance from JSON data."""
      return Turn(id = json['id'], name = json['name'], start_time = json["start_time"], end_time = json["end_time"], matchs = json["matchs"])
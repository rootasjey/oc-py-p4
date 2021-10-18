# -*- coding: utf-8 -*-

class Player:
  """Player class who can participate to a chess game."""
  def __init__(self, id = None, first_name = "", 
                    last_name = "", birth_date = "", sex = "", elo = 0):
    self.id = id
    self.birth_date = birth_date
    self.first_name = first_name
    self.last_name = last_name
    self.sex = sex
    self.elo = elo
    self.name = f"{first_name} {last_name}"

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    self._name = value

  def __str__(self):
    return f"{self.id} {self.first_name} {self.last_name} {self.birth_date} {self.sex} {self.elo}"
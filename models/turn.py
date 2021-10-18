from dataclasses import dataclass

@dataclass(unsafe_hash=True)
class Turn:
  name: str
  matchs: list
  start_date: str
  end_date: str


  def __init__(self):
        # Create games
      self.matchs = []
      return

  def create_match(self, p1, p2):
      self.matchs.append(([p1, 0], [p2, 0]))
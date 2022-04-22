class Band:
  def __init__(self, name, members):
      self.name = name
      self.members = members

  def play_solos(self):
    for member in self.members:
      pass

class Musician:
  def __init__(self, name):
      self.name = name

  def __str__(self):
      return f"My name is {self.name} and I play {self.get_instrument()}"

class Guitarist(Musician):
  def get_instrument(self):
    return 'guitar'

  def __repr__(self):
      return f"Guitarist instance. Name = {self.name}"

class Bassist(Musician):
  def get_instrument(self):
    return 'bass'

  # def __str__(self):
  #     return f"My name is {self.name} and I play {self.get_instrument()}"

  def __repr__(self):
      return f"Bassist instance. Name = {self.name}"

class Drummer(Musician):
  def get_instrument(self):
    return 'drums'

  # def __str__(self):
  #     return f"My name is {self.name} and I play {self.get_instrument()}"

  def __repr__(self):
      return f"Drummer instance. Name = {self.name}"

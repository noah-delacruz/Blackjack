# Class to reprsent individual cards
class Card:
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def __str__(self):
    return self.suit + self.value
# Class to represent individual cards
class Card:

  # Constructor
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  # How card is displayed when print is called
  def __str__(self):
    return self.value + " of " + self.suit
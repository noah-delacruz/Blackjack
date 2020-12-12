# Class to represent hand of cards

# inherit card class
from Card import Card

class Hand:

  # Constructor
  def __init__(self, isDealer):
    self.isDealer = isDealer
    self.cards = []
    self.value = 0

  # Adds card to hand
  def addCard(self, card):
    self.cards.append(card)

  # Helper function to calculate hand value
  def calculateHandValue(self):
    self.value = 0;
    hasAce = False

    for card in self.cards:
      # Adds face value of number card
      if card.value.isnumeric():
        self.value += int(card.value)
      # Adds values for ace, king, queen, jack
      else:
        # Adds value of ace
        if card.value == "A":
          hasAce = True
          self.value += 11
        # If not ace then card has to be a face card
        else:
          self.value += 10
    
    # Adjusts ace value if current hand with ace results in a bust
    if hasAce and self.value > 21:
      self.value -= 10
  
  # Getter function for hand value
  def getHandValue(self):
    self.calculateHandValue()
    return self.value
  
  # Displays hands of the dealer and player
  def showHand(self):
    if self.isDealer:
      print(self.cards[0])
      print("Unknown")
    else:
      for card in self.cards:
        print(card)
      print("Hand Value: ", self.getHandValue())
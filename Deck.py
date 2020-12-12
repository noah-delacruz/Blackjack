# Class to represent deck of 52 cards

# inherit card class
from Card import Card
# for random function to shuffle deck
import random

class Deck:

  # Constructor
  def __init__(self):
    self.deck = []
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values =  ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # Creates all 52 combinations of cards for deck
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit, rank))

  # Randomly shuffles deck
  def shuffle(self):
    random.shuffle(self.deck)
  
  # Gives card on top of the deck
  def hit(self):
    return self.deck.pop();



# Class to represent the Blackjack game and its logic

from Card import Card
from Deck import Deck
from Hand import Hand
import random

class Game:

  # Constructor
  def __init__(self):
    pass
  
  def runGame(self):
    keepPlaying = True

    # Create stats for player
    print("Welcome to Blackjack!")
    playerName = input("What is your name? ")
    cashAmount = int(input("How much money would you like to play with? "))
    playerWins = 0;
    playerLosses = 0;
    ties = 0;

    while keepPlaying:
      # Ask for bet amount
      betAmount = int(input("How much would you like to bet? "))
      cashAmount -= betAmount

      # Create deck and shuffle it
      self.deck = Deck()
      self.deck.shuffle()

      # Create hand objects for dealer and player
      self.playersHand = Hand(isDealer=False)
      self.dealersHand = Hand(isDealer=True)

      # Deal 2 cards to dealer and player
      for i in range(2):
        self.playersHand.addCard(self.deck.hit())
        self.dealersHand.addCard(self.deck.hit())

      # Show hands of dealer and player
      print("Dealer's hand is: ")
      self.dealersHand.showHand()
      print()
      print("Your hand is: ")
      self.playersHand.showHand()

      # Loop for players turn
      stopGame = False
      while not stopGame:
        # Check if either dealer or player has blackjack
        playerHasBlackjack, dealerHasBlackjack = self.checkForBlackjack()
        if playerHasBlackjack or dealerHasBlackjack:
          stopGame = True
          if playerHasBlackjack and dealerHasBlackjack:
            print("Both players have blackjack and thus there is a draw!")
            ties += 1
            cashAmount += betAmount
          elif playerHasBlackjack:
            print("You have blackjack! You win and the dealer loses!")
            playerWins += 1
            cashAmount += betAmount * 2
          elif dealerHasBlackjack:
            print("Dealer has blackjack! You lose and the dealer wins!")
            playerLosses += 1
          # Print stats
          print(playerName)
          print("Wins: ", playerWins)
          print("Losses: ", playerLosses)
          print("Ties: ", ties)
          print("Cash: ", cashAmount)
          print()
          print("Dealer")
          print("Wins: ", playerLosses)
          print("Losses: ", playerWins)
          print("Ties: ", ties)
          continue

        # Ask player if they want to hit or stand
        choice = input("Do you want to hit or stand? (h/hit or s/stand) ")
        choice = choice.lower()
        while choice not in ["h", "s", "hit", "stand"]:
          choice = input("That is not a valid input! Please choose to hit or stand: ")
          choice = choice.lower()
        
        # Deal card if player chooses to hit
        if choice == "hit" or choice == "h":
          self.playersHand.addCard(self.deck.hit())
          self.playersHand.showHand()
          # Check if player has busted after adding card
          if self.playersHand.getHandValue() > 21:
            print("You busted and therefore have lost!")
            stopGame = True
        # Option if player chose to stand
        else:
          playerHandValue = self.playersHand.getHandValue()
          dealerHandValue = self.dealersHand.getHandValue()

          print("Dealer's hand value: ", dealerHandValue)
          print("Your hand value: ", playerHandValue)

          if playerHandValue > dealerHandValue:
            print("You win and the dealer loses!")
            playerWins += 1
            cashAmount += betAmount * 2
          elif playerHandValue == dealerHandValue:
            print("Tie!")
            ties += 1
            cashAmount += betAmount
          else:
            print("You lose and the dealer wins!")
            playerLosses += 1
          
          # Print stats
          print(playerName)
          print("Wins: ", playerWins)
          print("Losses: ", playerLosses)
          print("Ties: ", ties)
          print("Cash: ", cashAmount)
          print()
          print("Dealer")
          print("Wins: ", playerLosses)
          print("Losses: ", playerWins)
          print("Ties: ", ties)
          
          stopGame = True
      
      playAgain = input("Do you want to play again? (y/yes or n/no) ")
      playAgain = playAgain.lower()
      while playAgain not in ["y", "yes", "n", "no"]:
        playAgain = input("This is not a valid input! Please enter y or n: ")
        playAgain = playAgain.lower()
      if playAgain == "y":
        gameOver = True
      else:
        print("Game will now end. Thank you!")
        keepPlaying = False

  # Checks if either dealer or player has blackjack
  def checkForBlackjack(self):
    if self.playersHand.getHandValue() == 21:
      playerBlackjack = True
    else:
      playerBlackjack = False
    
    if(self.dealersHand.getHandValue() == 21):
      dealerBlackjack = True
    else:
      dealerBlackjack = False

    return playerBlackjack, dealerBlackjack
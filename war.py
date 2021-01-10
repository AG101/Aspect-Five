# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:06:57 2020

@author: Aspect

Rules: (taken from bicyclecards.com)
The goal is to be the first player to win all 52 cards

THE DEAL
The deck is divided evenly, with each player receiving 26 cards, dealt one at a time, face down. Anyone may deal first. Each player places their stack of cards face down, in front of them.

THE PLAY
Each player turns up a card at the same time and the player with the higher card takes both cards and puts them, face down, on the bottom of his stack.

If the cards are the same rank, it is War. Each player turns up one card face down and one card face up. The player with the higher cards takes both piles (six cards). If the turned-up cards are again the same rank, each player places another card face down and turns another card face up. The player with the higher card takes all 10 cards, and so on.

HOW TO KEEP SCORE
The game ends when one player has won all the cards.

(not so interactive as it plays itself, but the game War is basically on autopilot when you play in real life anyway)
    
    
"""

import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = ("Spades", "Hearts", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card:
    '''
    creates attirubutes that all cards will have
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit



class Deck:
    '''
    instantiates a deck iterating through each suit and each rank, creating a created card for each then appending it to the list of all cards
    '''
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle_cards(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop()
    
class Player:
    
    def __init__(self, name):
        
        self.name = name 
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self, new_cards):
        #if its multiple cards we use extend to add those to the list(using append would append a list making it nested)
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
    
    
player_one = Player("Player One")
player_two = Player("Player Two")
the_deck = Deck()
the_deck.shuffle_cards()
for cards in the_deck.all_cards[0::2]:
    player_one.add_cards(the_deck.deal_one())
    player_two.add_cards(the_deck.deal_one())

round_number = 0
game_on = True
while game_on:
    
   round_number += 1
   print(f"Round: {round_number}")
   print(player_one)
   print(player_two)
   
   if len(player_one.all_cards) == 0:
       print(f"Player one is out of cards! Player Two wins!")
       break
   if len(player_two.all_cards) == 0:
       print(f"Player two is out of cards! Player One wins!")
       break
   
   player_one_cards = []
   player_one_cards.append(player_one.remove_one())
   
   player_two_cards = []
   player_two_cards.append(player_two.remove_one())
   
   at_war = True
   
   while at_war:
       
       if player_one_cards[-1].value > player_two_cards[-1].value:
           
           player_one.add_cards(player_one_cards)
           player_one.add_cards(player_two_cards)
           at_war = False
           
       elif player_two_cards[-1].value > player_one_cards[-1].value:
           
           player_two.add_cards(player_one_cards)
           player_two.add_cards(player_two_cards)
           at_war = False
           
       else:
           print("WARRRRRRRR!!R!R!R!R!R!R!R!R!R!R!R!")
           
           if len(player_one.all_cards) < 7:
               print("player one doesn't have enough cards, palyer two wins")
               game_on = False
               break
           elif len(player_two.all_cards) < 7:
               print("Player two has run out of cards, player one wins!")
               game_on = False
               break
           else:
               for num in range(7):
                   player_one_cards.append(player_one.remove_one())
                   player_two_cards.append(player_two.remove_one())
           
       
  
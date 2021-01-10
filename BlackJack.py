# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:36:17 2020

@author: Aspect

Black Jack

I have made blackjack and it has as many house rules as monopoly does so these are the ones that I will be 
working with

Rule variants:
    Aces high
    Dealer only shows 1 card on player turn, both + more on dealers turn
    Dealer hits until 17
    Player wins on a tie
    Zero chips = game over

"""

import random

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
suits = ("Spades", "Hearts", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

class Card:
    #creates attirubutes that all cards will have
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    #instantiates a deck iterating through each suit and each rank, creating a created card for each 
    #then appending it to the list of all cards
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle_cards(self):
        #shuffles the deck
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop()

class Player:
    
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []
        self.bet_amount = 0
    
    def bet(self):
        #sets the players bet, not allowing them to bet more than they have or input invalid values
        while True:
            try:
                self.bet_amount = int(input("How much would you like to bet? "))
                if self.bet_amount <= player_1.chips:
                    print(f"You are betting {self.bet_amount} chips worth")
                    break
                else:
                    print("You do not have enough chips")
                    continue
            except ValueError:
                print("Please enter integers")
                continue
        return self.bet_amount      
    
    def bust_check(self):
        #runs after each card is dealt, if any hand total reaches 21 or higher the game ends
        bust = 0
        for i in player_1.hand[0::]:
            bust += i.value
        if bust >= 21:
            return True
        
    def hand_total(self):
        #contains the total value of a given hand, used to compare dealer and players hand if the player hasn't 
        #gone bust, the dealer hasn't gone bust and the dealers hand value is >= 17
        total = 0
        for i in self.hand[0::]:
            total += i.value
        return total
    
    def hit(self):
        #allows the player to hit until they bust or choose to stick
        #if the player busts, chips betted are subtracted from their total
        while True:
            answer = input("Do you wish to hit(h) or stick(s)")
            if answer == 'h' or answer == 'hit':
                print("you have chosen to hit, heres another card")
                self.hand.append(the_deck.deal_one())
                print("Your new hand is: ")
                for i in self.hand:
                    print(i)
                
                if self.bust_check():
                    self.chips = self.chips - self.bet_amount
                    print(f"You have gone bust, round over and you now have {self.chips} chips remaining")
                    break
                else:
                    continue
            elif answer == 's' or answer == 'stick':
                print("you have chosen to stick, Dealers turn")
                break
            else:
                print("Answer must be a hit or a stick, please try again")
                continue
        return self.chips
    
    def dealer_lost(self):
        #if the dealer loses a hand, the players bet is added to their chip total
        self.chips += self.bet_amount
        print(f"The dealer has gone bust, you now have {self.chips} chips remaining")
        return self.chips
    
    def player_lost(self):
        #if the player loses a hand, the players bet is subtracted from their chip total
        #here because the player can lose without busting
        self.chips -= self.bet_amount
        print(f"The player has lost, you now have {self.chips} chips remaining")
        return self.chips
    
    def clear_hand(self):
        #clears hand for a new round
        self.hand = []
    
    def game_check(self):
        #checks to see if the player wishes to continue playing after each round, providing they have enough chips
        while True:
            ans = input("Do you wish to keep playing? y/n")
            if ans == 'y':
                keep_playing = True
                break
            elif ans == 'n':
                keep_playing = False
                break
        return keep_playing
    def game_finished(self):
        print(f"Thanks for playing {self.name}! Your chips total to: {self.chips}, cash out soon!")
    
    def no_more_chips(self):
        print(f"Thanks for playing {self.name}! Your chip total is 0, thanks for playing.")

    def __str__(self):
        return f"{self.name} has the {self.hand[0]} and the {self.hand[1]} in their hand."

class Dealer:
    
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def clear_hand(self):
        #used to clear dealers hand for new round
        self.hand = []
        
    def show_dealer_hand(self):
        #only 1 card is displayed of the dealers during the players turn, on the dealers turn the whole hand 
        # is displayed
        print("This is the dealer's hand: ")
        for i in self.hand:
            print(i)
            
    def bust_check(self):
        #runs after each card is dealt, if any hand total reaches 21 or higher the game ends
        bust = 0
        for i in self.hand[0::]:
            bust += i.value
        if bust >= 21:
            return True
    def dealer_check(self):
        #the dealer will stop drawing cards after its hand value, exceeds 17, this keeps track of that
        hit_17 = 0
        for i in self.hand[0::]:
            hit_17 += i.value
        if hit_17 >= 17:
            return True
    def dealer_hit(self):
        #the dealer will hit providing it hasn't busted and its hand value is lower than 17
        while True:
            self.hand.append(the_deck.deal_one())
            self.show_dealer_hand()
            if self.bust_check():
                print("The dealer has gone bust, you win!")
                break
            elif self.dealer_check():
                print("Dealer has reached the 17 limit, lets compare")
                break
            else:
                continue
    def hand_total(self):
        #contains the total value of a given hand, used to compare dealer and players hand if the player hasn't 
        #gone bust, the dealer hasn't gone bust and the dealers hand value is >= 17
        total = 0
        for i in self.hand[0::]:
            total += i.value
        return total
        
    def __str__(self):
        return f"{self.name} has the {self.hand[0]} and an unknown facedown card in their hand."

#initialise the deck
the_deck = Deck()

#shuffle the deck
the_deck.shuffle_cards()

#initialise the player and the dealer
player_1 = Player("Alex", 10)
print(f"You have {player_1.chips} chips to start with") #player needs to know how many chips they are starting with
the_dealer = Dealer("The Dealer")

#boolean to toggle game
game_on = True

while game_on:
    #player bets first(before they even see their cards, heart of the cards!)
    player_1.bet()
    
    #deal 2 cards each to player and dealer
    for i in range(2):
        player_1.hand.append(the_deck.deal_one())
    for i in range(2):
        the_dealer.hand.append(the_deck.deal_one())
    
    #show both hands(in dealers case only the first card is shown)
    print(the_dealer)
    print(player_1)
    
    #offer player 1 a chance to hit/stick
    player_1.hit()
    
    #checks if the player has any chips left, 0 chips = game over
    if player_1.chips == 0:
        player_1.no_more_chips()
        break
    
    #checks whether the player has busted
    if player_1.bust_check():
        #if p1 busts, both hands are cleared 
        player_1.clear_hand()
        the_dealer.clear_hand()
        #p1 is aksed if they'd like to continue playing, if so, next round commences
        if player_1.game_check():
            continue
        else:
            #if not game over and final message printed
            player_1.game_finished()
            break
    #now we can see both of the dealers cards
    the_dealer.show_dealer_hand()
    #dealer auto hits till they reach 17-20 where they stick or 21+ where they bust
    the_dealer.dealer_hit()
    #runs when the dealer busts
    if the_dealer.bust_check():
        #if dealer busts, print a message, update chips, clear hands, ask player if they want continue
        player_1.dealer_lost()
        player_1.clear_hand()
        the_dealer.clear_hand()
        if player_1.game_check():
            #game continues
            continue
        else:
            #game over
            player_1.game_finished()
            break
    #soft 17 check, if they haven't busted they'll have to be somewhere between 17 and 20    
    elif the_dealer.dealer_check():
        #hand values are compared, playerwins, chips updated, hands cleared, game continues or quits
        if player_1.hand_total() >= the_dealer.hand_total():
            print("Player wins this round")
            player_1.dealer_lost()
            player_1.clear_hand()
            the_dealer.clear_hand()
            if player_1.game_check():
                continue
            else:
                player_1.game_finished()
                break
        #hand values compared, dealerwins, chips updates, hands cleared, game continues or quits
        #player wins in the event of a tie
        elif the_dealer.hand_total() > player_1.hand_total():
            print("Dealer wins this round")
            player_1.player_lost()
            player_1.clear_hand()
            the_dealer.clear_hand()
            if player_1.game_check():
                continue
            else:
                player_1.game_finished()
                break
        


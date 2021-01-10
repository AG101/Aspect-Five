# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:16:21 2020

@author: Aspect

"""

board_list = ["1","2","3","4","5","6","7","8","9"]
lst = ["","","","","","","","",""]

def display_board(board_list): 
    #displays a 3 by 3 tic-tac-toe board to the users, with numbers 1-9 in playable spots
    
    print("   " + "  !  " + "   !   " + "   ")   
    print("  " + board_list[0] + "  !  " + board_list[1] + "  !  " + board_list[2])
    print("   " + "  !  " + "   !   " + "   ") 
    print("-----------------")
    print("   " + "  !  " + "   !   " + "   ")   
    print("  " + board_list[3] + "  !  " + board_list[4] + "  !  " + board_list[5])
    print("   " + "  !  " + "   !   " + "   ") 
    print("-----------------")
    print("   " + "  !  " + "   !   " + "   ")   
    print("  " + board_list[6] + "  !  " + board_list[7] + "  !  " + board_list[8])
    print("   " + "  !  " + "   !   " + "   ")    


def choose():
#introduces the game and invites Player 1 to choose noughts or crosses
#first here referes to it being the first or opening move of the game
    first = 'wrong'
    
    while first not in ['O', 'X', 'x', 'o']:
        first = input("Welcome to Noughts and Crosses, Player 1, choose 'O' or 'X'")    
        if first not in ['O', 'X', 'x', 'o']:        
            print("sorry invalid")
        
    if first == 'o' or first == 'O':
        print("Player 1 has chosen O, Player 2 will be X")
        noughts = True
    elif first == 'x' or first == 'X':
        print("Player 1 has chosen X, Player 2 will be O")
        noughts = False
        
    return noughts

    
def player_choice(noughts):
#invites players to choose a spot on the board to place their piece, the numbered choices are shown on the board
#and are contained in the list: board_list. as players make their choice, the numbers in board_list are replaced
#with x's or o's, a position can only be selected if it still has a number in that position     
    choice = 'wrong'
    
    if noughts:
        player = "1"
    if not noughts:
        player = "2"
        
    while choice not in board_list:
        choice = input(f"Player{player} Pick a position on the board: ")
        if choice not in board_list:    
            print("sorry invalid")
        
    return int(choice)

    
def replacement_choice(board_list, position,noughts):
#whose turn it is, is stored in the noughts variable 
    
    if noughts:
        user_placement = 'O'
    else:
        user_placement = 'X'
#acounts for lists/arrays indexing from 0 so that users can use 1-9 instead of 0-8    
    board_list[position-1] = user_placement
    
    return board_list


def turn_switcher(noughts):
#switches turns    
    if noughts:
        noughts = False
    elif not noughts:
        noughts = True
    
    return noughts

def win_check(board_list, win, noughts):
#all of the win coindtitions, there is probably a better way to do this    
    if board_list[0] == 'O' and board_list[1] == 'O' and board_list[2] == 'O':
        win = True
    elif board_list[3] == 'O' and board_list[4] == 'O' and board_list[5] == 'O':
        win = True
    elif board_list[6] == 'O' and board_list[7] == 'O' and board_list[8] == 'O':
        win = True
    elif board_list[0] == 'O' and board_list[3] == 'O' and board_list[6] == 'O':
        win = True
    elif board_list[1] == 'O' and board_list[4] == 'O' and board_list[7] == 'O':
        win = True    
    elif board_list[2] == 'O' and board_list[5] == 'O' and board_list[8] == 'O':
        win = True
    elif board_list[0] == 'O' and board_list[4] == 'O' and board_list[8] == 'O':
        win = True
    elif board_list[6] == 'O' and board_list[4] == 'O' and board_list[2] == 'O':
        win = True
    elif board_list[0] == 'X' and board_list[1] == 'X' and board_list[2] == 'X':
        win = True
    elif board_list[3] == 'X' and board_list[4] == 'X' and board_list[5] == 'X':
        win = True
    elif board_list[6] == 'X' and board_list[7] == 'X' and board_list[8] == 'X':
        win = True
    elif board_list[0] == 'X' and board_list[3] == 'X' and board_list[6] == 'X':
        win = True
    elif board_list[1] == 'X' and board_list[4] == 'X' and board_list[7] == 'X':
        win = True    
    elif board_list[2] == 'X' and board_list[5] == 'X' and board_list[8] == 'X':
        win = True
    elif board_list[0] == 'X' and board_list[4] == 'X' and board_list[8] == 'X':
        win = True
    elif board_list[6] == 'X' and board_list[4] == 'X' and board_list[2] == 'X':
        win = True
        
    if win:
        if noughts:
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    return win

# initialisation + logic
win = False
display_board(board_list)
noughts = choose()

while not win:
    position = player_choice(noughts)
    board_list = replacement_choice(board_list, position, noughts)
    display_board(board_list)
    win = win_check(board_list, win, noughts)
    noughts = turn_switcher(noughts)
# -*- coding: utf-8 -*-
#
# ps10pr3.py (Problem Set 10, Problem 3)
### Author: Evelyn Baranski (evelynb@bu.edu), 8/7/21
# Playing the game
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    

#Main Function given
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
        

#Process move function 
def process_move(p, b):
    """Takes two parameters: a player object, p, for the player whose move is
    being processed and a Board object b for the board at which the game is being
    played"""
    
    #Print message specifiying whose turn it is
    print(str(p) + "'s turn")
    
    #Calls the next move function, and stores its value
    next_move = p.next_move(b)
    
    #applying the appropraite move to the board, calling add checker
    b.add_checker(p.checker, int(next_move))
    
    #printing a blank line and then the board
    print()
    print(b)
    
    #checking to see if the move resulted in a win or a tie, calling is_win_for
    if b.is_win_for(p.checker):
        #Printing if its a win in the number of moves
        print(str(p), 'wins in', str(p.num_moves), 'moves.')
        print('Congratulations!')
        return True     #returning True if its a win
    
    #if the move results in not a win, but the board is full, printing its a tie
    elif b.is_full():
        print("It's a tie!")
        return True
    
    #otherwise, returning False if not a win or tie
    else:
        return False
    



if __name__ == '__main__':
    b1 = Board(2, 4)
    b1.add_checkers('001122')
    print(b1)
    
    #process_move(Player('X'), b1)
    
    #process_move(Player('O'), b1)
    
    b1.remove_checker(3)
    b1.remove_checker(3)
    
    process_move(Player('O'), b1)
    process_move(Player('X'), b1)

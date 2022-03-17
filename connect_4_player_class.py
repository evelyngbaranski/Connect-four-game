# -*- coding: utf-8 -*-
#
## Author: Evelyn Baranski (evelynb@bu.edu), 8/7/21
# A Connect Four Player class 
#

from ps10pr1 import Board


class Player:
    
    
    #Constructor
    def __init__(self, checker):
        """Constructor for the new Player object initalizes the
        checker attribute and the number of moves attribute"""
        
        assert(checker ==  'X' or 'O')
        
        #Checker is a one character string representing the game
        #piece for the player
        self.checker = checker
        
        #Integer stores the number of moves the player has made
        #initialized to zero since player has not made any moves
        #yet
        self.num_moves = 0
        
        
    
    #Method 1
    def __repr__(self):
        """Method returns a string to represent a Player object
        string indicates which checker the Player object is using"""
        
        #returns "Player X" or "Player O"
        return 'Player ' + self.checker
    
    
    
    #Method 2
    def opponent_checker(self):
        """Method returns a one character string representing the
        checker of the Player object's opponent"""
        
        #if Player's checker is O, the opponent is X
        if self.checker == 'O':
            return 'X'
        
        #otherwise, the opponent is O
        return 'O'
    
    
    #Method 3
    def next_move(self, b):
        """Method accepts a board object, b, as a parameter and
        returns the column where the player wants to make the next 
        move. Method asks the user to input a column number representing
        where they want to place the checker on the board"""
        
        #adding 1 to the number of moves
        self.num_moves += 1
        
        #asking the user to input the column of their choice
        #and making the inputed string an integer
        col = int(input('Enter a column: '))
        
        #Using the can_add_to method to see if its a valid column
        #if user can add to column, returns the column, otherwise
        #returns "Try again!"
        if b.can_add_to(col):
            return col
        else:
            return 'Try again!'     
            col = int(input('Enter a column: '))
 
        

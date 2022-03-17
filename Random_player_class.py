# -*- coding: utf-8 -*-
##Author: Evelyn Baranski (evelynb@bu.edu), 8/12/21
#
# A RandomPlayer for use in Connect Four
#

import random
from ps10pr3 import * # to use the connect_four and process_move functions


#Defining the class, random player as a subclass of Player
class RandomPlayer(Player):
    
    
    #Method to override the next_move method inherited from Player
    def next_move(self, board):
        """Overrides the next move method inherited from player
        rather than asking the user for their next move,
        this version should choose at random from the columns 
        that are not full yet and return the index of that 
        randomly selected column"""
        
        
        #incremeting the number of moves that RandomPlayer object has made
        self.num_moves += 1
        
        #initializing col, an empty list for the indices
        col = []
        
        #for x in range of the board width
        for x in range(board.width):
            
            #calling can add to, for if its a possible move
            if board.can_add_to(x):
                #if so adding its index to the list
                col += [x]
        
        #calls a random choice from the list of columns and returns
        c = random.choice(col)
        return c 

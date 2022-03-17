# -*- coding: utf-8 -*-
#Evelyn Baranski - 
#
# An AI Player for use in Connect Four
#

import random
from ps10pr3 import * # to use the connect_four and process_move functions


#Part 1:
#Creating AIPlayer as a subclass of Player
class AIPlayer(Player):
    
    
    #Part 2:
    def __init__(self, checker, tiebreak, lookahead):
        """Constructor to create a new AIPlayer object"""
        
        #assert statements that validate the inputs
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        #calling Player constructor to initailize the attributes 
        #inherited from that class
        Player.__init__(self, checker)
        
        #Initializing the new attributes, tiebreak and lookahead
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    
    
    #Part 3:
    def __repr__(self):
        """Overrides __repr__ from Player, indicates tiebreaking 
        strategy and lookahead"""
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
    
    
    
    
    #Part 4:
    def max_score_column(self, scores):
        """takes a list, scores, containing a score for each column
        on the board, and that reutrns the index of the column with
        the maximum score. if one or more columns are tied for the
        max score, should aply the called tiebreaking strategy
        to break the tie."""
        
        #getting the maximum score from scores 
        m = max(scores)
        #Creating empty list
        list_ch = []
        
        #for x in range of the scores
        for x in range(len(scores)):
            #if the score == maximum score, adding value to list
            if scores[x] == m:
                list_ch += [x]
        
        #If tie breaking strategy is left
        if self.tiebreak == 'LEFT':
            #returning left play
            return list_ch[0]
        
        #if tie breaking strategy is right
        if self.tiebreak == 'RIGHT':
            #returning right play
            return list_ch[-1]
        
        #otherwise if tie breaking straegy is random
        else:
            #returning a random choice from list
            return random.choice(list_ch)
    
    
    #Part 5:
    def scores_for(self, board):
        """Takes a Board object, board, am determines the called
        AIPlayer's scores for the columns in board. Each column
        is assigned one of four possible scores. Method returns
        a list containing one score for each column"""
        
        #creating a list of scores with the length of board width
        scores = [0] * board.width
        
        
        #for column in range of board width
        for col in range(board.width):
            
            #If the column is full, assigning a score of -1
            if board.can_add_to(col) == False:
                scores[col] = -1
            
            #if board is already a win for player's opp., 
            #assigning score 0
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            
            #If board is already a win from called AI player, 100 to col
            elif board.is_win_for(self.checker):
                scores[col] = 100
            
            #If lookahead is 0, assigning score of 50 to column
            elif self.lookahead == 0:
                scores[col] = 50
            
            #OTHERWISE, looking ahead
            else:
                #adding a checker to the column
                board.add_checker(self.checker, col)
                
                #creating an opponent player to get the opponent scores
                #of the move
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead - 1))
                opponent_scores = opponent.scores_for(board)
                
                #If the move is a win for the opponent, assigning
                #value of 0 to the column
                if max(opponent_scores) == 100:
                    scores[col] = 0
                
                #If the move is a win for AIPlayer, assigning
                #value of 100 to the column
                elif max(opponent_scores) == 0:
                    scores[col] = 100
                
                #if column is full for opp. assigning -1 for move
                elif max(opponent_scores) == -1:
                    scores[col] = -1
                
                #Otherwise, assignging columns to 50 like in previous part
                else:
                    scores[col] = 50
                
                #Removing the checker / move from the board
                board.remove_checker(col)
        #Returning the list of scores
        return scores
    
    
    #Part 6 
    def next_move(self, board):
        """Overrides the next_move method. Rather than asking
        the user for the next move, version of next move should
        return AIPlayer's judgement of the best possible move."""
        
        #adding 1 to the number of moves for the AIPlayer
        self.num_moves += 1
        
        #returning the max score col from the called scores for list
        return self.max_score_column(self.scores_for(board))
    
    

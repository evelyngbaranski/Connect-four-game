# -*- coding: utf-8 -*-
#
### Author: Evelyn Baranski (evelynb@bu.edu), 8/7/21


#This file is craeting the Class Board

class Board:
    
    #1: 
    def __init__(self, height, width):
        """Initializing the board"""
        
        #Initializing the height, the number of rows on the board
        self.height = height
        
        #Initializing the width, the number of columns on the board
        self.width = width
        
        #initializing slots, stores a reference to a 2D list with
        #height rows and width columns used to store the contents of 
        #the board
        self.slots = [self.width*[' '] for row in range(self.height)]
            #board is initally empty so it has space characters
  
    
    #Method 2:
    def __repr__(self):
        """Prints the string form of the connect four board"""
        
        #beginning with an empty string
        s = ''
        
        #for each row in range of height, add one row of slots at a time
        for row in range(self.height):
            s += '|'  #one vertical bar at the start of the row
            
            #for column in range of width
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            
            s += '\n'  #newline at the end of the row
        
        #adding the hyphens at the bottom of the board 
        s += '-' * (self.width*2 + 1) #length of width x 2 + 1
        
        #adding a newline at the end of the hyphens
        s += '\n'
            
        #For statement to add the column numbers to bottom of board
        for n in range(self.width):
            #if n is greater than 9, restarting count at 0
            if n > 9:
                n = n - 10
            #adding space between each number
            s += ' '
            
            #adding the string of n
            s += str(n)
        
        return s 
    
    
    #Method 2:
    def add_checker(self, checker, col):
        """adds specified checkers (X or O) to specified position 
        on the board"""
        
        #assert statement to validate the inputs for the parameters
        #checker and col
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        
        row =  0 #starting row with a value of zero
        
        #while statement adding 1 to value of row
        while self.slots[row][col] == ' ' and row < (self.height - 1):
            row += 1
        if row == (self.height - 1) and self.slots[self.height - 1][col] == ' ':
            row += 1
        self.slots[row - 1][col] = checker
        
    
    #Method 3:
    def reset(self):
        """resets the board of checker, clearing all the spots and
        adding ' '(a space)"""
        
        #for the height and width making slots = a space to reset board
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '


    
    #Method 4: given
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'."""
        
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    
    #Method 5: 
    def can_add_to(self, col):
        """Returns True if it is valid to place a checker in that column,
        otherwise, returns False"""
        
        #if column is greater than or equal to zero and less than the
        #width of the board. Makes so column # isn't too low or high
        if col >= 0 and col < self.width:
            
            #if placement at row zero (the top row) and column is a space
            #returns true that the player can place their piece
            if self.slots[0][col] == ' ':
                return True
            else:
            #otherwise, returns False
                return False
    
   
    #Method 6
    def is_full(self):
        """Returns True if the called Board object is completely full
        of checkers, and returns False otherwise"""
        
        #for column in the range of the width of the board
        for c in range(self.width):
            
            #calls can add to to see if column is full, returning False
            #if not full
            if self.can_add_to(c):
                return False
        
        #otherwise, returns True
        return True
    
    
    
    #Method 7
    def remove_checker(self, col):
        """Removes the top checker of the column, c, of the called
        Board object. If the column is empty, than it should do 
        nothing"""
        
        for r in range(self.height):
            
            #if the placement does not equal a space
            if self.slots[r][col] != ' ':
                
                #removes the top placement, replaces with space
                self.slots[r][col] = ' '
                return self
            

    
    
    #Method 8: all of the win function for is_win_for
    #Horizontal win
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
    """
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True

    # if we make it here, there were no horizontal wins
        return False
    
    #Vertical win
    def is_vertical_win(self, checker):
        """Checks for a vertical win for a specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width):
            #check if the next four rows in the column
            #contain the specified character
                if self.slots[row][col] == checker and \
                self.slots[row+1][col] == checker and \
                self.slots[row+2][col] == checker and \
                self.slots[row + 3][col] == checker:
                    return True
            
       #if we make it here, there were no vertical wins 
        return False

    #left diagonal win
    def is_left_diagonal_win(self, checker):
        """Checks for a left diagonal win for a specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
            #check if the next four rows and columns -3 for diagonal
            #contain the specified character
                if self.slots[row][col] == checker and \
                self.slots[row + 1][col + 1] == checker and \
                self.slots[row  + 2][col + 2 ] == checker and \
                self.slots[row + 3][col + 3] == checker:
                    return True
        
        #if we make it here, there were no left diagonal wins
        return False
    
    #right diagonal win
    def is_right_diagonal_win(self, checker):
        """Checks for a rigth diagonal win for a specified checker"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
            #check if the next four rows and columns have a diagonal
            #win
                if self.slots[row][col] == checker and \
                self.slots [row - 1][col +1] == checker and \
                self.slots[row - 2][col + 2] == checker and \
                self.slots[row - 3][col + 3] == checker:
                    return True
        
        #if we make it here, there were no right diagonal wins
        return False
    
    #Method for is_win_for
    def is_win_for(self, checker):
        """accepts parameter, 'X' or 'O', and returns True if there
        are four consequtive slots containing checker on the board,
        otherwise returns False"""
        
        assert(checker == 'X' or checker == 'O')
        # call the helper functions and use their return values to
        # determine whether to return True or False
        
        #if it is a horizontal, vertical, right diagonal, or left diagonal win
        #returns True
        if self.is_horizontal_win(checker) or self.is_vertical_win(checker) or\
        self.is_right_diagonal_win(checker) or self.is_left_diagonal_win(checker):
            return True
        
        #otherwise, returns False, (no win)
        else:
            return False



            

                
if __name__ == '__main__':
    b = Board(5, 5)
    
    b.add_checker('X', 1)
    b.add_checker('X', 2)
    b.add_checker('X', 2)
    b.add_checker('O', 3)
    b.add_checker('X', 3)
    b.add_checker('X', 3)
    b.add_checker('O', 4)
    b.add_checker('X', 4)
    b.add_checker('O', 4)
    b.add_checker('X', 4)
    
    print(b)
    
    print(b.is_win_for('X'))
    
        
        
            

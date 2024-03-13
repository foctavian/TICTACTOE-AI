import numpy as np
from constants import X, O
COLS =3 
ROWS =3 
class Board():
    def __init__(self):
        self.marked = np.zeros((3,3))
        self.no_marked = 0
        self.empty = self.marked
        
    def __str__(self):
        return str(self.marked)    
    
    def mark(self, row, col, player):
        self.marked[row][col] = player
        self.no_marked += 1
        
    def is_full(self):
        return self.no_marked == 9
    
    def is_empty(self):
        return self.no_marked == 0
    
    def player_mark(self, row, col):
        return self.marked[row][col]
    
    def get_all_possible_moves(self):
        moves = []
        for row in range(3):
            for col in range(3):
                if self.marked[row][col] == 0:
                    moves.append((row,col))
        return moves
    
    def copy(self):
        copy = Board()
        copy.marked = np.copy(self.marked)
        copy.no_marked = self.no_marked
        return copy
    
    def check_board_state(self):
        #straigth lines
            #rows
        for row in range(3):
            if self.marked[row][0] == self.marked[row][1] == self.marked[row][2] != 0:
                return X if self.marked[row][0] == X else O
                
            #columns
        for col in range(3):
            if self.marked[0][col] == self.marked[1][col] == self.marked[2][col] != 0:
                return X if self.marked[0][col] == X else O
                
            #diagonals
        if self.marked[0][0] == self.marked[1][1] == self.marked[2][2] != 0:
            return X if self.marked[0][0] == X else O
        if self.marked[2][0] == self.marked[1][1]==self.marked[0][2] != 0:
            return X if self.marked[2][0] == X else O
        return None
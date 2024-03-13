from board import Board
import copy
import numpy as np
from constants import X, O

class AI():
    def __init__(self, player=O, level=1):
        self.level = level
        self.player = player
        
    def random_move(self, board):
        moves = board.get_all_possible_moves()
        move = moves[np.random.randint(len(moves))]
        return move
    def minimax(self, board, maximizing):
        state = board.check_board_state()
        if state == 1:
            return 1, None
        elif state == 2:
            return -1, None
        elif board.is_full():
            return 0, None
        if maximizing:
                max_eval = -100
                best_move = None
                empty_sqrs = board.get_all_possible_moves()

                for (row, col) in empty_sqrs:
                    temp_board = copy.deepcopy(board)
                    temp_board.mark(row, col, 1)
                    eval = self.minimax(temp_board, False)[0]
                    if eval > max_eval:
                        max_eval = eval
                        best_move = (row, col)
                return max_eval, best_move
        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_all_possible_moves()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
            board.mark(best_move[0], best_move[1], O)
            return min_eval, best_move
        
        
    def eval(self,board):
        eval, move = self.minimax(board, False)
        print(eval, move)
        return move
 
                
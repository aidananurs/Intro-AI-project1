"""
Created on Thu Mar 17 17:02:48 2022

@author: Aidana
"""
from copy import deepcopy
import pygame
from checkers.constants import ROWS, COLS, BLUE, WHITE, BLACK, GREEN, RED, RADIUS


def minimax(position, depth, max_player, game):
    position.goalstate()
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        return maxEval, best_move
    else:
        #should that be float('inf'), just without minus sign
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, GREEN, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
            return minEval, move
        
        

def get_all_moves(board, colour, game):
    moves = []
    
    #getting current position for each peg
    for peg in board.get_all_pegs(colour):
        #getting valid moves for each peg
        valid_moves = board.get_valid_moves(peg)
        #print(valid_moves)
        for row, col in valid_moves:
            temp_board = deepcopy(board)
      
            temp_peg = deepcopy(peg)
            temp_peg_row = deepcopy(row)
            temp_peg_col = deepcopy(col)

            temp_peg = temp_board.get_peg(peg.row, peg.col)
            #create new board after moving
            new_board = do_move(temp_peg, temp_peg_row, temp_peg_col, temp_board, game)
            moves.append(new_board)
    return moves

def do_move(peg, row, col, temp_board, game):   
    temp_board.move(peg, row, col)
    return temp_board

        
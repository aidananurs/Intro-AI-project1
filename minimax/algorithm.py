"""
Created on Thu Mar 17 17:02:48 2022

@author: Aidana
"""
from copy import deepcopy
import pygame
from .constants import ROWS, COLS, BLUE, WHITE, BLACK, GREEN, RED, RADIUS

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    if max_player:
        maxEval = float('-inf')
        best_move_row = None
        best_move_col = None
        for move, row, col in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move_row = row
                best_move_col = col
        return maxEval, best_move_row, best_move_col
    else:
        minEval = float('-inf')
        best_move_row = None
        best_move_col = None
        for move in get_all_moves(position, GREEN, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(maxEval, evaluation)
            if minEval == evaluation:
                best_move_row = row
                best_move_col = col
            return minEval, best_move_row, best_move_col
        
        

def get_all_moves(board, colour, game):
    moves = []
    
    #getting current position for each peg
    for peg in board.get_all_moves(colour):
        #getting valid moves for each peg
        valid_moves = board.get_valid_moves(peg)
        for row, col in valid_moves:
            temp_board = deepcopy(board)
            #temp_peg = temp_board.get_peg(row, col)
            #create new board after moving
            new_board = do_move(peg, row, col, temp_board, game)
            moves.append([new_board, row, col])
    return moves

def do_move(peg, row, col, temp_board, game):
    temp_board.move(peg, row, col)
    return temp_board;
        
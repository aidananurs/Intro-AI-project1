"""
Created on Thu Mar 17 17:02:48 2022

@author: Aidana
"""
from copy import deepcopy
import pygame
from .constants import ROWS, COLS, BLUE, WHITE, BLACK, GREEN, RED, RADIUS
from checkers.board import Board
board=Board()

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
       
    else:   


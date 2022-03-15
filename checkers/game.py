# -*- coding: utf-8 -*-
import pygame
from .constants import GREEN,RED,GREY,RADIUS
from checkers.board import Board
from checkers.drawing_transition_matrix import x_cord,y_cord

#board=Board()

class Game:
    def __init__(self,win):
        self._init()
        self.win = win
        
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = GREEN
        self.valid_moves = {}
        
    def reset(self):
        self._init()
    
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        #else:
        peg = self.board.get_peg(row,col)
        if peg != 0 and peg.color == self.turn:
            self.selected = peg
            self.valid_moves = self.board.get_valid_moves(peg)
            return True
        
        return False
    
    def _move(self, row, col):
        peg = self.board.get_peg(row,col)
        if self.selected and peg == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        return True
    
    def draw_valid_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win,GREY,(x_cord[row,col],y_cord[row,col]),RADIUS//3,0 )
    
    def change_turn(self):
        if self.turn == GREEN:
            self.trun = RED
        else:
            self.trun = GREEN
            
            
            
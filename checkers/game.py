# -*- coding: utf-8 -*-
import pygame
from .constants import GREEN, RED, GREY, RADIUS
from checkers.board import BoardClass
from checkers.drawing_transition_matrix import x_cord, y_cord


class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    #updating the game window     
    def update(self):
        self.board.draw(self.win, self.selected)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = BoardClass()
        self.turn = GREEN
        self.valid_moves = []
    #checking the winning conditions    
    def winner(self):
        return self.board.winner()    
    #selecting the peg, checking valid moves for it and drawing them
    def select(self, row, col):
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        peg = self.board.get_peg(row, col)
        if peg != 0 and peg.color == self.turn:
            self.selected = peg
            self.valid_moves = self.board.get_valid_moves(peg)
            return True

        return False
    #Making the move of selected peg (only human player)
    def move(self, row, col):
        if self.selected and not self.board.get_peg(row, col) and [row, col] in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
            self.board.goalstate()
        else:
            return False
        return True
    #Drawing valid moves with grey circles
    def draw_valid_moves(self, moves):
        if moves is None:
            return
        for singleMove in moves:
            row, col, = singleMove[0], singleMove[1]
            pygame.draw.circle(self.win, GREY, (x_cord[row, col], y_cord[row, col]), RADIUS // 3, 0)
    #Changing the active player turn
    def change_turn(self):
        self.valid_moves = []
        if self.turn == GREEN:
            self.turn = RED
        else:
            self.turn = GREEN
    #Returning the board class        
    def get_board(self):
        return self.board
    #Making move for the AI
    def ai_move(self,board):
        self.board = board
        self.board.goalstate()
        self.change_turn()                 
                       
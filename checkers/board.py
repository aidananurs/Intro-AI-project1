# -*- coding: utf-8 -*-
import pygame
from .constants import ROWS,COLS,BLUE,WHITE,BLACK,GREEN,RED,RADIUS
from .drawing_transition_matrix import x_cord, y_cord
from .start_board import size, start_board
from .pegs import Peg

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.green_left = 6
        self.create_board()
    def draw_circles(self,win):
        win.fill(BLUE)
        for row in range(ROWS):
            for col in range(COLS):
              pygame.draw.circle(win,WHITE,[x_cord[row,col],y_cord[row,col]],RADIUS,0)
    def move(self, peg, row, col):
        self.board[peg.row][peg.col], self.board[row][col] = self.board[row][col], self.board[peg.row][peg.col]
        peg.move(row,col)
        
    def get_peg(self,row,col):
        return self.board[row][col] 
        
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if start_board[row,col]==1:
                    self.board[row].append(Peg(row,col, RED))
                elif start_board[row,col]==2:
                    self.board[row].append(Peg(row,col, GREEN))
                else:
                    self.board[row].append(0) 
    def draw(self,win):
        self.draw_circles(win)
        for row in range(ROWS):
            for col in range(COLS):
                Peg = self.board[row][col]
                if Peg != 0:
                    Peg.draw(win)
        
                
                    
# -*- coding: utf-8 -*-
import pygame
import numpy as np
from .constants import ROWS, COLS, BLUE, WHITE, BLACK, GREEN, RED, RADIUS
from .drawing_transition_matrix import x_cord, y_cord
from .start_board import size, start_board
from .pegs import Peg


class BoardClass:
    def __init__(self):
        self.board = []
        self.red_ingoal = self.green_ingoal = 0
        self.create_board()

    def draw_circles(self, win):
        win.fill(BLUE)
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.circle(win, WHITE, [x_cord[row, col], y_cord[row, col]], RADIUS, 0)

    def move(self, peg, row, col):
        self.board[peg.row][peg.col], self.board[row][col] = self.board[row][col], self.board[peg.row][peg.col]
        peg.move(row, col)

    def get_peg(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if start_board[row, col] == 1:
                    self.board[row].append(Peg(row, col, RED))
                elif start_board[row, col] == 2:
                    self.board[row].append(Peg(row, col, GREEN))
                else:
                    self.board[row].append(0)
                    
    def draw(self, win, selected):
        self.draw_circles(win)
        for row in range(ROWS):
            for col in range(COLS):
                Peg = self.board[row][col]
                if Peg != 0:
                    Peg.draw(win, selected)
                    
    def goalstate(self):
        self.red_ingoal = self.green_ingoal = 0
        for i in range(ROWS):
            for j in range(COLS):
                peg=self.board[i][j]
                if peg !=0:
                    if peg.color == RED and start_board[i,j] == 2:
                        self.red_ingoal += 1
                    if peg.color ==  GREEN and start_board[i,j] == 1:
                        self.green_ingoal += 1 
        
    def winner(self):
        if self.red_ingoal == 6:
            print('RED WINS')
            return RED
        elif self.green_ingoal == 6:
            print('GREEN WINS')
            return GREEN
        
        return None

    def get_valid_moves(self, Peg):
        moves = []
        row = Peg.row
        col = Peg.col

        #all hopOne moves
        moves = self.hopOne(row, col)

        moves = self.hopOver(row, col, moves)


        return moves

    def hopOne(self, row, col):
        moves = []
        # down
        if row + 1 <= 5 and self.board[row + 1][col] == 0:
            moves.append([row + 1, col])
        # up
        if row - 1 >= 0 and self.board[row - 1][col] == 0:
            moves.append([row - 1, col])
        # right
        if col + 1 <= 5 and self.board[row][col + 1] == 0:
            moves.append([row, col + 1])
        # left
        if col - 1 >= 0 and self.board[row][col - 1] == 0:
            moves.append([row, col - 1])

        return moves

    def hopOver(self, row, col, moves):

        if row + 2 <= 5 and self.board[row + 1][col] != 0 and self.board[row + 2][col] == 0 and [row + 2, col] not in moves:
            moves.append([row + 2, col])

            moves = self.hopOver(row + 2, col, moves)

        if row - 2 >= 0 and self.board[row - 1][col] != 0 and self.board[row - 2][col] == 0 and [row - 2, col] not in moves:
            moves.append([row - 2, col])

            moves = self.hopOver(row - 2, col, moves)

        if col + 2 <= 5 and self.board[row][col + 1] != 0 and self.board[row][col + 2] == 0 and [row, col + 2] not in moves:
            moves.append([row, col + 2])

            moves = self.hopOver(row, col + 2, moves)

        if col - 2 >= 0 and self.board[row][col - 1] != 0 and self.board[row][col - 2] == 0 and [row, col - 2] not in moves:
            moves.append([row, col - 2])

            moves = self.hopOver(row, col-2, moves)
        return moves
    
    def get_all_pegs(self, colour):
        pegs = []
        for row in self.board:
           for peg in row:
               if peg != 0 and peg.color == colour:
                   pegs.append(peg)
        return pegs
    
    def get_board(self):
        return self.board
    
    def evaluate(self):
        h=0
        for i in range(ROWS):
            for j in range(COLS):
                peg=self.board[i][j]
                if peg != 0:
                    if peg.color == RED:
                        h+=(5-j)+i
                    if peg.color == GREEN:
                        h-=j+(5-i)
        self.goalstate()
        h+=5*self.red_ingoal
        h-=5*self.green_ingoal    
        return h    


    #TODO Should we add the code to identify the winning position?
    #TODO method that returns all pieces(pegs) (e.g. current positions of either first or second player's pegs). How we identify them? By colour or just by 1,2?
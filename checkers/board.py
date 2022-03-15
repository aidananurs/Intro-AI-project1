# -*- coding: utf-8 -*-
import pygame
from .constants import ROWS,COLS,BLUE,WHITE,BLACK,GREEN,RED,RADIUS
from .drawing_transition_matrix import x_cord, y_cord
from .start_board import size, start_board
from .pegs import Peg

class Board:
    def __init__(self):
        self.board = []
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
                   
    
    def get_valid_moves(self, Peg):
        moves = {}
        left = Peg.row - 1
        right = Peg.col + 1
        row = Peg.row
        col = Peg.col
        moves.update(self._traverse_left(col-1, max(row-3,-1), -1, Peg.color, left))
        moves.update(self._traverse_right(row-1, max(row-3,-1), -1, Peg.color, right))
        moves.update(self._traverse_left(col+1, min(row+3,ROWS), 1, Peg.color, left))
        moves.update(self._traverse_right(row+1, min(row+3,ROWS), 1, Peg.color, right))
        
        return moves
   
    def _traverse_left(self, start, stop, step, color, left, skipped = []):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if left >= ROWS:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)] = last + skipped
                else:
                    moves[(r,left)] = last
                    
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3,ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1, skipped = last))    
                    moves.update(self._traverse_right(r+step, row, step, color, left+1, skipped = last))
                break
            #if u can't jump over your pegs             
            # elif current.color == color:
            #     break
            else:
                last = [current]
            left += 1
        return moves
    
    def _traverse_right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for r in range(start,stop,step):
            if right < 0:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r,right)] = last
                    
                if last:
                    if step == -1:
                        row = max(r-3,0)
                    else:
                        row = min(r+3,ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1, skipped = last))    
                    moves.update(self._traverse_right(r+step, row, step, color, right+1, skipped = last))
                break
            #if u can't jump over your pegs            
            # elif current.color == color:
            #     break
            else:
                last = [current]
            right -= 1
            
        return moves



        
                
                    
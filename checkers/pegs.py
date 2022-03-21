# -*- coding: utf-8 -*-
import pygame
from .constants import BLUE,RADIUS,BLACK
from .drawing_transition_matrix import x_cord, y_cord


class Peg:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.goal = False
        self.x = 0
        self.y = 0
        self.calc_pos()
    #Calculating posistion of the peg in x,y coordinate of the window in order to draw them.    
    def calc_pos(self):
        self.x = x_cord[self.row, self.col]
        self.y = y_cord[self.row, self.col]
    #Drawing pegs and little circle in the currently selected peg
    def draw(self, win, Peg):
        if Peg is not None and self.row == Peg.row and self.col == Peg.col:
            pygame.draw.circle(win, self.color, (self.x, self.y), RADIUS, 0)
            pygame.draw.circle(win, BLUE, (self.x, self.y), RADIUS/2, 0) 
            pygame.draw.circle(win, BLACK, (self.x, self.y), RADIUS + 2, 1)
            return
        pygame.draw.circle(win, self.color, (self.x, self.y), RADIUS, 0)
        pygame.draw.circle(win, BLACK, (self.x, self.y), RADIUS + 2, 1)
    #assinging the row and column of the space that we moved to to the peg
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

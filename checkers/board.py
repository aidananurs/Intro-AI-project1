# -*- coding: utf-8 -*-
import pygame
from .constants import *

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.blue_left = 6
        x_max=WIDTH
        y_max=HEIGHT
        x_cord,y_cord = 0,40
    def draw_circles(self,win):
        win.fill(BLUE)
        for i in range(1,5):
            for j in range(1,i):
              pygame.draw.circle(win,WHITE,[400-20*j,j*40],RADIUS,0)

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:26:11 2022

@author: Karol
"""

import pygame
from checkers.constants  import WIDTH,HEIGHT
from checkers.board import Board
from checkers.drawing_transition_matrix import x_cord,y_cord

FPS = 30

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chineese Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    if x>=400 and y>=400:
        col = x-400 // 60
        row = y-400 //60
    elif x>400 and y<400:
        col = x-400 //60
        row = 400-y // 60
    elif x<400 and y<400:
        col = 400-x //60
        row = 400-y // 60
    elif x<400 and y>400:
        col = 400-x //60
        row = y-400 // 60
    return row,col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    
    # peg = board.get_peg(0,4)
    # board.move(peg,0,3)
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                peg = board.get_peg(row,col)
                board.move(peg,0,3)
        board.draw(WIN)
        pygame.display.update()
    
    pygame.quit()
    
main()
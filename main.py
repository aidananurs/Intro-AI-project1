# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:26:11 2022

@author: Karol
"""

import pygame
from checkers.constants import WIDTH, HEIGHT, RADIUS, GREEN, RED
from checkers.drawing_transition_matrix import x_cord, y_cord
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chineese Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    for i in range(len(x_cord)):
        for j in range(len(x_cord)):
            if ((x - x_cord[i, j]) ** 2 + (y - y_cord[i, j]) ** 2) < RADIUS ** 2:
                return i, j
    return False


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        #print(game.turn)
        #if computer
        if game.turn == RED:
            #value, row, col = minimax(game.get_board(), 3, True, game)
            value, new_board = minimax(game.get_board(), 3, True, game)
            #game.moveAI(row, col)
            #I think we should just return the whole new board (list of object)
            #instead of row and col, just like guy from YT
            #game.ai_move is simply assigning the new board that is a result of 
            #an algorithm to existing one.
            #The update function handles drawing everything
            game.ai_move(new_board)
            
        if game.winner() !=None:
           # print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pegPositionInMatrix = get_row_col_from_mouse(pos)
                if not pegPositionInMatrix:
                    break
                game.select(pegPositionInMatrix[0], pegPositionInMatrix[1])

        game.update()

    pygame.quit()


main()

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 12:26:11 2022

@author: Karol
"""

import pygame
from checkers.constants import WIDTH, HEIGHT, RADIUS, GREEN, RED
from checkers.drawing_transition_matrix import x_cord, y_cord
from checkers.game import Game

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

    # peg = board.get_peg(0,4)
    # board.move(peg,0,2)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pegPositionInMatrix = get_row_col_from_mouse(pos)

                if not pegPositionInMatrix:
                    break

                if game.turn == GREEN:
                    game.select(pegPositionInMatrix[0], pegPositionInMatrix[1])

                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # peg = board.get_peg(row,col)
                # board.move(peg,0,2)
        game.update()

    pygame.quit()


main()
# -*- coding: utf-8 -*-
# from start_board import size,pegs,start_board
# from checkers.constants import HEIGHT,WIDTH,DIAMETER, H_MARGIN
import numpy as np
# size=6
# pegs=int(size/2)
# x_cord=np.ones((size,size))*400
# y_cord=np.zeros((size,size))-DIAMETER-H_MARGIN
# for i in range(size-1,-1,-1):
#     for j in range(size):
#         x_cord[i,j]=int(WIDTH/2)-(j)*(DIAMETER+H_MARGIN)
        
# for i in range(size-1,-1,-1):
#     for j in range(size):
#         if i==(size-j-1):
#             x_cord[i,j]=400
        
#BRUTE FORCE
x_cord= np.array(
        [[750, 680, 610, 540, 470, 400],
         [680, 610, 540, 470, 400, 330],
         [610, 540, 470, 400, 330, 260],
         [540, 470, 400, 330, 260, 190],
         [470 ,400, 330, 260, 190, 120],
         [400, 330, 260, 190, 120, 50]])
y_cord= np.array(
        [[420, 490, 560, 630, 700, 770],
         [350, 420, 490, 560, 630, 700],
         [280, 350, 420, 490, 560, 630],
         [210, 280, 350, 420, 490, 560],
         [140, 210, 280, 350, 420, 490],
         [70, 140, 210, 280, 350, 420]])

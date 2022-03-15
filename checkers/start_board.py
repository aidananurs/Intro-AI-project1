import numpy as np
size=6
pegs=int(size/2)
start_board=np.zeros((size,size))
for i in range(pegs-1,size):
    for j in range(i-pegs+1):
        start_board[i,j]=1
        start_board[size-i-1,size-j-1]=2
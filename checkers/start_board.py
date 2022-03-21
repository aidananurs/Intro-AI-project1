#Making the inicial state matrix with 0 as no peg in certain position  
#and 1 and 2 when there is either red of green peg
import numpy as np
size=6
pegs=int(size/2)
start_board=np.zeros((size,size))
for i in range(pegs-1,size):
    for j in range(i-pegs+1):
        start_board[i,j]=1
        start_board[size-i-1,size-j-1]=2
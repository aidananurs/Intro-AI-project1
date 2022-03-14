import numpy as np
import math
from Board import size

def evaluation(A=[]):
        h=0
        for i in range(size):
            for j in range(size):
                if A[i,j]==1:
                    h=h+np.sqrt(((size-i-1)^2)+((size-j-1)^2))
                    h=h+np.sqrt(((size-i-1)^2)+((size-j-1)^2))
        return h                      
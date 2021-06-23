from math import floor, sqrt
from numpy import zeros

def solution(n):

    # Z[k] = (maximal staircase length) + 1 with k blocks
    Z = [floor((sqrt(8*k+1)+1)/2) for k in range(n)]
    C = zeros([n,n], dtype = int)

    # C[i,j] = number of staircases with (i+1) blocks & final step height ≤ j
    for i in range(n):
        for j in range(Z[i],i+1):
            C[i,j] = sum(C[i-k,k-1] for k in range(Z[i],j+1))
        for j in range(i+1,n):
            C[i,j] = C[i,i]+1
            
    return C[n-1,n-1]

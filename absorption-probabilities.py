import numpy as np
from math import gcd

def solution(M):

    n = len(M)
    M = np.array(M)
    ps = []
    t_states = [i for i in range(n) if sum(M[i]) == 0] # index terminal states
    for j in range(n):
        # correct terminal states with probability 1 along diagonal
        # subtract identity matrix except for terminal state rows
        M[j,j] = 1 if j in t_states else M[j,j] - sum(M[j])

    # get relevant entries of inverse (top row, columns w/ terminal indices)
    for t in t_states:
        m = []
        for k in [i for i in range(n) if i != t]:
            m.append(M[k,1:n])
        p = abs(round(np.linalg.det(np.array(m)))) if n != 1 else 1
        ps.append(p)
    # compute determinant of full matrix to scale entries above
    dt = abs(round(np.linalg.det(np.array(M)))) if n != 1 else 1
    ps.append(dt)

    s = ps[0]
    for i in range(len(ps)):        
        s = gcd(s, ps[i])

    return [p//s for p in ps]

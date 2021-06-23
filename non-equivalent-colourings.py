from collections import Counter
from numpy import prod
from math import factorial, gcd

# distinct partitions of the integer n of length z
# additional entry needed for passing to recursion
def partition(n,m,z):
    if n <= m:       
        yield [n]
    for x in range(min(n-1,m),max(0,(n-1)//z),-1):
        for pt in partition(n-x, x, z-1):
            yield [x] + list(pt)

# this is just an application of the cycle index computation technique
# for number of colours c and two partitions (one row direction, one column), this finds and
# evaluates the corresponding polynomial term (of the Polya polynomial/cycle index) at c
def term(rw,cl,c):
    k = 0
    for t in rw[1]:
        for s in cl[1]:
            k = k + gcd(s[0],t[0])*s[1]*t[1]
    return rw[0]*cl[0]*c**k

# for each partition of some integer n, this outputs the number of symmetries the partition,
# i.e. the coefficient of the cycle index, output along the partition itself (for computation of the polynomial terms)
def sym(n):
    
    s = []
    for pt in partition(n,n,n):
        cts = Counter(pt)
        part_counts = []
        
        # describe each partition pt as a set of tuples (x,y) where, for each tuple:
        # x is a value in the partition pt
        # y is the number of times x occurs in the partition pt
        for k in list(cts):
            part_counts.append((k,cts[k]))

        # compute symmetries of partition viewed as a row (or column), each distinct value representing its own colour
        # do not remove int(), long_scalar overflow issue appears otherwise
        p = factorial(n)//prod(pt)
        r = prod([factorial(cts[n]) for n in cts])
        s.append((int(p//r), part_counts))
    return s

# sum terms of polynomial given row, column, colour numbers, divide by symmetry group size 
def solution(M,N,c):
    row = sym(M)
    col = sym(N)
    total = 0
    for rw in row:
        for cl in col:
            total = total + term(rw,cl,c)
    return total//(factorial(M)*factorial(N))

# returns 1 iff (a,b) cycle, 0 otherwise
def loops(a,b):
    n = a+b
    while n%2 == 0:
        n = n//2
    return int((a%n)*(b%n) != 0)

# find pair in list with first entry matching a given integer
def find(z,lst):
    for tpl in lst:
        if loops(tpl[0],z) == 1:
            return tpl
    return 0
      
def solution(lst):
    cts = set()
    # record number of times integer x appears in list
    for x in lst:
        cts.add((x,lst.count(x)))
    ls = list(cts)
    
    # sort increasing 
    ls.sort(key = lambda x: x[0])
    imposs = 0
    L = len(ls)
    
    while L > 0:
        x = ls[0]
        
        # get next element, check whether it loops with further elements
        # if so remove all instances of both, else record as being impossible
        nxt = find(x[0],ls)
        if nxt != 0:
            m = min(nxt[1],x[1])
            ls[ls.index(nxt)] = (nxt[0],nxt[1] - m)
            z = next(s for s in ls if s[0] == x[0])
            ls[ls.index(z)] = (z[0], z[1] - m)
            ls = [i for i in ls if i[1] != 0]
        else:            
            imposs = imposs + x[1]
            ls.pop(ls.index(x))
        L = len(ls)
        
    return imposs


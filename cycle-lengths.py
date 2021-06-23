# converts to base d (from decimal)
def conv(n,d):
    
    br = []
    while n >= d:
        (n, r) = divmod(n,d)
        br.append(r)
    br.append(n)   
    br = reversed(br)
    new = [str(i) for i in br]
    return ''.join(new)

def solution(n,b):

    k = len(n)    
    L = ['0']
    
    while n not in L:        
        lst_n = list(n)
        if k != len(n):
            lst_n = ['0' for i in range(k - len(lst_n))] + lst_n            
        n = ''.join(lst_n)
        L.append(n)
        asc = [int(i) for i in sorted(lst_n)]
        des = list(reversed(asc))
        n = conv(sum((asc[j] - des[j])* b ** j for j in range(k)), b)
               
    return len(L) - L.index(n) if int(n) != 0 else 1


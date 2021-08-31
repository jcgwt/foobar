from collections import Counter

# returns 1 iff (a,b) cycle, 0 otherwise
def loops(a,b):
    if a*b == 0:
        return False
    n = a+b
    while n%2 == 0:
        n = n//2
    return int((a%n)*(b%n) != 0)

# outer loop indexed by ex_it runs through list; at each increment inner loop indexed by in_it
# checks whether the relevant terms loop and adds those that do to the counter, removing the appropriate amounts
# increment ex_it if the value at this index (number of players not paired up with others) reach 0, or if ex_it
# reaches the end of the list
def solution(lst):
    lst = [list(pair) for pair in Counter(lst).most_common()]
    lst.sort(key = lambda p: -p[1])
    imposs = 0
    N = len(lst)
    ex_it = 0
    while ex_it < N:
        in_it = ex_it
        while in_it < N:
            x = lst[ex_it][1]
            y = lst[in_it][1]
            if loops(lst[ex_it][0],lst[in_it][0]):
                lst[ex_it][1] = max(x-y,0)
                lst[in_it][1] = max(y-x,0)
                if lst[ex_it][1] == 0:
                    break
            in_it += 1
        imposs += lst[ex_it][1]
        ex_it += 1
    return imposs
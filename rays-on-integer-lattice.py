from math import sqrt, gcd

# euclidean distance between X and Y
def eucl(X,Y):
    return sqrt((X[0]-Y[0])**2 + (X[1]-Y[1])**2)

# unit vector between target and reference
def unit(pt,rf):
    d = max(abs(gcd((pt[0] - rf[0]), (pt[1] - rf[1]))),1)
    return ((pt[0] - rf[0]) // d, (pt[1] - rf[1]) // d)

# parameters: room, reference point, target point, distance travellable by beam
def solution(rm,rf,tgt,ds):
    pts = [] 
    drct = set() # directions to targets; set() for avoid duplicates & is-in check
    for p in range((rf[0] - ds) // rm[0], (rf[0] + ds) // rm[0] + 1):
        for q in range((rf[1] - ds) // rm[1], (rf[1] + ds) // rm[1] + 1):            
            e = (int(rm[0]*(p+p%2)+(-1)**p*tgt[0]),int(rm[1]*(q+q%2)+(-1)**q*tgt[1]))
            m = (int(rm[0]*(p+p%2)+(-1)**p*rf[0]),int(rm[1]*(q+q%2)+(-1)**q*rf[1]))
            # list of target points (index by 1) and reachable points (indexed by 0)
            pts.extend([
                        [1,e,eucl(e,rf)],
                        [0,m,eucl(m,rf)]
                        ])
    # sort by euclidean distance
    pts.sort(key = lambda x: x[2])
    valid_targets = 0
    for pt in pts:
        if pt[2] <= ds:
            u = unit(pt[1],rf)
            # add suitable unit vectors (pointing to target & within range)
            if u not in drct:
                drct.add(u)
                valid_targets = valid_targets + pt[0]
        else:
            break
    return valid_targets

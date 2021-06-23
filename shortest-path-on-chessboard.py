def solution(dim,A,B):

    # mirror to upper quadrant
    x = abs(A[0] - B[0])
    y = abs(A[1] - B[1])
    corners = [(i,j) for i in [0,dim[0]-1] for j in [0,dim[1]-1]]
    c = 0 if A in corners or B in corners else 1
    # if in the neighbourhood of Knight, adjust if at a corner
    if (x,y) in [(0,1), (1,0), (2,2), (1,1)]:        
        return 4 - ((x + y) % 2) - 2 * c

    # in frame, separate according to whether in the bands parallel to x-y axes
    else:    
        s = (x + y + 1) // 3   
        m = s + ((x + y) % 3 + 1) // 2
        return m if max(x,y) <= 2 * s else m + 2 * ((max(x,y) + 3 - 2 * m) // 4)

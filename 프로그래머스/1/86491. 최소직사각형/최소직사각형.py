def solution(sizes):
    a,b  = 0,0
    for i,j in sizes:
        a = max(max(i,j),a)
        b = max(min(i,j),b)
    return a*b
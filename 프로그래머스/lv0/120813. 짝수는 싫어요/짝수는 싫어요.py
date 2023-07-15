def solution(n):
    if n == 1:
        return [1]
    return [i for i in range(1,n+1,2)]
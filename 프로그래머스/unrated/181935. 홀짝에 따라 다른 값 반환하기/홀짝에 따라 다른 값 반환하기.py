def solution(n):
    if n % 2 == 0:
        return sum([i**2 for i in range(n,0,-2)])
    else:
        return sum([i for i in range(n,0,-2)])
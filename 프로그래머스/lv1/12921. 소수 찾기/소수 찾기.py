def primeNum(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if primeNum(i):
            answer += 1
    return answer
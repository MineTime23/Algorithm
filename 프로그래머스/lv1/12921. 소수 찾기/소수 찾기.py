def primenum(num):
    if num == 2:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2,n+1):
        if primenum(i):
            answer += 1
    return answer
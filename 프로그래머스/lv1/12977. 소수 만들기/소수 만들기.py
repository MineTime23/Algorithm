import itertools 
def primeNum(n):
    if n == 2 or n == 3:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        
def solution(nums):
    answer = 0
    for i in itertools.combinations(nums,3):
        if primeNum(sum(i)):
            answer += 1
    return answer
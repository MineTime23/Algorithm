import itertools

def primenum(num):
    if num == 2:
        return True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in itertools.combinations(nums,3):
        if primenum(sum(i)):
            answer += 1
    return answer
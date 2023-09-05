import itertools 

def prime_num(n):
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    result = set()
    for i in range(1,len(numbers)+1):
        for res in itertools.permutations(numbers, i):
            if prime_num(int(''.join(res))):
                result.add(int(''.join(res)))
    return len(result)
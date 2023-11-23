def judg(num):
    if num <= 3:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return True
    return False

def solution(n):
    answer = 0
    for i in range(1,n+1):
        if judg(i):
            answer += 1
    return answer
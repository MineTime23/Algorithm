def solution(n):
    answer = 1
    temp = 1
    while temp <= n:
        temp *= answer
        answer += 1
    return answer-2
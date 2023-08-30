def solution(n,a,b):
    answer = 1
    temp = 2
    a -= 1
    b -= 1
    while a//temp != b//temp:
        temp *= 2
        answer += 1
    return answer
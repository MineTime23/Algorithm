def solution(n):
    answer = 2
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    for i in range(2,n):
        if n % i == 0 and i % 2 == 1:
            answer += 1 
    if n % 2 == 0:
        answer -= 1
    return answer
def solution(n):
    answer = 1
    while (answer * n) % 6 != 0:
        answer += 1
    return (answer * n)//6
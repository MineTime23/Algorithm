def solution(n):
    answer = ""
    while n // 3 != 0:
        answer += str(n%3)
        n //= 3
    answer += str(n)
    return int(answer, 3)
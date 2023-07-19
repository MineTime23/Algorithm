def solution(n):
    answer = ""
    while n != 0:
        answer += f"{n%3}"
        n = n // 3
    return int(answer,3)
def solution(num):
    answer = 0
    while answer != 501 and num != 1:
        answer += 1
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
    if num == 1:
        return answer
    return -1
def solution(x):
    res = 0
    for i in str(x):
        res += int(i)
    return x % res == 0
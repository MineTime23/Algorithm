def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    a = 2
    b = 3
    for i in range(n-3):
        a, b = b, a+b
    return b%1234567
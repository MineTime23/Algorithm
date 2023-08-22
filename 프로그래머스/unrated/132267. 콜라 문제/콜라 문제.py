def solution(a, b, n):
    answer = 0
    while n >= a:
        t = n//a
        answer += t*b
        n -= a*t
        n += t*b
    return answer
def solution(n):
    result = []
    while n != 0:
        result.append(n%3)
        n//= 3
    return int(''.join(map(str, result)),3)
def solution(n):
    result = set()
    while n != 1:
        for i in range(2,n+1):
            if n%i == 0:
                result.add(i)
                n //= i
                break
    return sorted(list(result))
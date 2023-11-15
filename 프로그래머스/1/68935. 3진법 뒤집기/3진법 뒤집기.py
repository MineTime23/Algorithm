def make_3(n):
    result = []
    while n != 0:
        result.append(str(n%3))
        n //= 3
    return ''.join(result)
        

def solution(n):
    return int(make_3(n),3)
def Primenum(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    result = ""
    while n != 0:
        result += str(n%k)
        n //= k
    result = result[::-1]
    result = result.split("0")
    for i in result:
        if i.isnumeric() and Primenum(int(i)):
            answer += 1
    return answer
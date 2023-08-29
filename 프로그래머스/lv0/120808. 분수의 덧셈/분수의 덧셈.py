import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    ma = denom1 * denom2 // math.gcd(denom1,denom2)
    answer = [numer1 * (ma // denom1) + numer2 * (ma // denom2), ma]
    Gcd = math.gcd(answer[0],answer[1])
    answer[0] //= Gcd
    answer[1] //= Gcd
    return answer
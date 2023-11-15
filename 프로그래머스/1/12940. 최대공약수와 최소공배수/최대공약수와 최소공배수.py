import math
def solution(n, m):
    Gcd = math.gcd(n,m)
    return [Gcd, n*m//Gcd]
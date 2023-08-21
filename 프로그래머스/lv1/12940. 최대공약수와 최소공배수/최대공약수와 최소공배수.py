import math
def solution(n, m):
    yak = math.gcd(n,m)
    return [yak, n*m//yak]
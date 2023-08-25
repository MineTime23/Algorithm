# 6과 n의 공배수
import math

def solution(n):
    return n*6//math.gcd(n,6)//6
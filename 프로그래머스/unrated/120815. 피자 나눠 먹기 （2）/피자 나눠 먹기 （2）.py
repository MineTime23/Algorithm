# 6 과 n의 최소공배수 / n
import math

def solution(n):
    return (6*n)//math.gcd(6,n)//6
import math

def solution(numer1, denom1, numer2, denom2):
    mom = denom1 * denom2 // math.gcd(denom1, denom2)
    result = [numer1*denom2 + numer2*denom1 , denom1 * denom2]
    
    return [result[0]//math.gcd(result[0],result[1]),result[1]//math.gcd(result[0],result[1])]
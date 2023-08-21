def solution(price, money, count):
    result = sum(range(price,price*count+1,price))
    return 0 if money > result else result-money
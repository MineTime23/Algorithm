def solution(brown, yellow):
    num = brown + yellow
    num2 = (brown + 4)//2
    for i in range(2, num):
        if num % i == 0 and (i + num//i) == num2:
            return [max(num//i,i),min(num//i,i)]
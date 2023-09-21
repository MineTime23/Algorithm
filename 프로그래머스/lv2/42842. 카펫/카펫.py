def solution(brown, yellow):
    sum_ab =(brown - 4)//2
    for i in range(1,int(yellow**0.5)+1):
        if yellow % i == 0:
            if i + (yellow//i) == sum_ab:
                return [(yellow//i)+2 ,i+2]
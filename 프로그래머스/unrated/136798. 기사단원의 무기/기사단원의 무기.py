def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        answer2  = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                answer2 += 1
                if j**2 != i:
                    answer2 += 1
            if answer2 > limit:
                answer2 = power
                break
        answer += answer2
    return answer
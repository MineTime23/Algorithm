def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            answer += 2
            #print(i)
    if int(n**0.5) == (n**0.5):
        answer -= 1
    return answer
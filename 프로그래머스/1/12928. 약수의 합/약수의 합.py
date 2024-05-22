def solution(n):
    answer = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 3
    
    
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            answer += i
            answer += (n//i)
    
    if int(n**0.5) == n **0.5:
        answer -= (n **0.5)
    return answer
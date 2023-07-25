def solution(n):
    
    if n == 1:
        return 1
    if n == 2:
        return 1

    
    answer = 1
    if n%2 == 1:
        answer += 1
    for i in range(3,n,2):
        if n%i == 0:
            answer += 1
            
    return answer
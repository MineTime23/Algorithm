def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for i in d:
        cnt += 1
        answer += i        
        if answer > budget:
            return cnt - 1
    return cnt
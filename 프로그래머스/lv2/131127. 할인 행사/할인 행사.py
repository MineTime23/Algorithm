from collections import Counter

def solution(want, number, discount):
    answer = 0
    result = []
    for a,b in zip(want, number):
        for _ in range(b):
            result.append(a)
    result = Counter(result)
    for i in range(len(discount)-9):
        res = Counter(discount[i:i+10])
        if result==res:
            answer += 1
        
    return answer
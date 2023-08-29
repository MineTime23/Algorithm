from collections import Counter

def solution(N, stages):
    People_num = len(stages)
    answer = []
    stages = Counter(stages)
    for i in range(1, N+1):
        answer.append((i,stages[i]/People_num if People_num else 0))
        People_num -= stages[i]
    answer = sorted(answer, key = lambda x : -x[1])
    return [a for a,b in answer]
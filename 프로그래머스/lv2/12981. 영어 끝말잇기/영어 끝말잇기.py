from collections import defaultdict

def solution(n, words):
    answer = []
    data1 = defaultdict(int)
    for i,v in enumerate(words):
        if data1[v] != 0:
            return [i%n + 1,i//n + 1]
        
        if len(v) == 1:
            return [i%n + 1,i//n + 1]
        
        if i == 0:
            data1[v] += 1
            answer.append(v)
        elif i != 0:
            if answer[-1][-1] != v[0]:
                return [i%n + 1,i//n + 1]
            else:
                data1[v] += 1
                answer.append(v)
    return [0,0]
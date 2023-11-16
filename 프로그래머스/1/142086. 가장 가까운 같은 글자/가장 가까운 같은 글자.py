from collections import defaultdict

def solution(s):
    answer = []
    s = " " + s
    data = defaultdict(int)
    for i,v in enumerate(s):
        if data[v] == 0:
            data[v] = i
            answer.append(-1)
        else:
            answer.append(i-data[v])
            data[v] = i
    return answer[1:]
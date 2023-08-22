from collections import defaultdict
def solution(s):
    answer = []
    s = " "+ s
    data = defaultdict(int)
    for i,v in enumerate(s):
        if i == 0:
            continue
        elif data[v] == 0:
            answer.append(-1)
        elif data[v] != 0:
            answer.append(i-data[v])
        data[v] = i 
    return answer
from collections import defaultdict

def solution(s):
    answer = []
    s = " " + s
    data = defaultdict(int)
    for i,a in enumerate(s):
        if a == " ":
            continue
        elif data[a] == 0:
            answer.append(-1)
            data[a] = i
        else:
            answer.append(i-data[a])
            data[a] = i
    return answer
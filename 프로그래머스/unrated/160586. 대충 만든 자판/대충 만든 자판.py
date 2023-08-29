from collections import defaultdict
def solution(keymap, targets):
    answer = []
    data = defaultdict(int)
    for i in keymap:
        for j in range(len(i)):
            if data[i[j]] == 0:
                data[i[j]] = j+1
            else:
                if j+1 <= data[i[j]]:
                    data[i[j]] = j+1
                    
    answer = []
    for i in targets:
        a = 0 
        for j in range(len(i)):
            if data[i[j]] == 0:
                a = -1
                break
            else:
                a += data[i[j]]
        if a == 0:
            a = -1
        answer.append(a)
    
    return answer
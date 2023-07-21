from collections import defaultdict
def solution(keymap, targets):
    answer = []
    data = defaultdict(int)
    for i in keymap:
        for j in range(len(i)):
            if data[i[j]] == 0:
                data[i[j]] = j+1
            else:
                data[i[j]] = min(data[i[j]], j+1)
    for i in targets:
        arr = list(map(lambda x : data[x] if data[x] != 0 else -1,list(i)))
        if -1 in arr:
            answer.append(-1)
        else:
            answer.append(sum(arr))
    return answer
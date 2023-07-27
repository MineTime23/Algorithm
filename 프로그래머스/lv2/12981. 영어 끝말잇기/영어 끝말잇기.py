from collections import defaultdict

def solution(n, words):
    data = defaultdict(int)
    for idx, item in enumerate(words):
        data[item] += 1
        result = True
        if data[item] == 2:
            res = idx
            result = False
            break
        if idx != 0 and item[0] != words[idx-1][-1]:
            res = idx
            result = False
            break
    return [0,0] if result else [res%n+1,res//n+1]

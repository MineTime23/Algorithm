from collections import defaultdict
def solution(s):
    result = []
    data = defaultdict(int)
    for i in range(len(s)):
        if i == 0:
            data[s[i]] = -1
            result.append(-1)
        elif data[s[i]] == 0:
            data[s[i]] = i
            result.append(-1)
        elif data[s[i]] == -1:
            data[s[i]] = i
            result.append(i)
        else:
            result.append(i-data[s[i]])
            data[s[i]] = i
    return result
from collections import defaultdict
def solution(clothes):
    data = defaultdict(int)
    for a,b in clothes:
        data[b] += 1
    result = list(data.values())
    #print(result)
    if len(result) == 1:
        return result[0]
    else:
        a = 1
        for i in result:
            a *= (i+1)
        return a-1

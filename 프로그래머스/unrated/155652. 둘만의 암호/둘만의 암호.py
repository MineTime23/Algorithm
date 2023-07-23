from collections import defaultdict
def solution(s, skip, index):
    answer = ''
    alpha = [chr(i+97) for i in range(26)]
    alpha = sorted(list(set(alpha)-set(skip)))
    data = defaultdict(int)
    for i,v in enumerate(alpha):
        data[v] = i
    for i in s:
        answer += alpha[(data[i]+index)%len(alpha)]
    return answer
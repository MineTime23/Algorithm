from collections import Counter

def solution(k, tangerine):
    answer = 0 
    cnt = 0
    tan = Counter(tangerine)
    tan = sorted(list(tan.items()), key = lambda x : -x[1])
    for a, b in tan:
        answer += b
        cnt += 1
        if answer >= k:
            return cnt
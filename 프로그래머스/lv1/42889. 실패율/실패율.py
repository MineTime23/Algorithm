from collections import Counter
def solution(N, stages):
    answer = []
    arr = Counter(stages)
    cnt = len(stages)
    for i in range(1,N+1):
        cnt2 = arr[i]
        answer.append((i,cnt2/cnt if cnt != 0 else 0))
        cnt -= cnt2
    return [a for a,b in sorted(answer,key = lambda x : (-x[1],x[0]))]
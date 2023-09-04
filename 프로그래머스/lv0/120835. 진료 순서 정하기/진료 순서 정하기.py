from collections import defaultdict
def solution(emergency):
    data = defaultdict(int)
    emer = sorted(emergency)
    for i,v in enumerate(emer):
        data[v] = len(emergency)-i
    return list(map(lambda x : data[x],emergency))
from collections import Counter
def solution(citations):
    total = len(citations)
    cal = Counter(citations)
    answer = 0
    for i in range(max(citations)+1):
        if total >= i:
            answer = i
        total -= cal[i]
    return answer
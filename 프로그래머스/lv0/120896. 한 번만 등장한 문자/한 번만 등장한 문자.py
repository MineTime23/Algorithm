from collections import Counter

def solution(s):
    answer = []
    result = Counter(s)
    print(result)
    for i in result.items():
        if i[1] == 1:
            answer.append(i[0])
    return ''.join(sorted(answer))
from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    data = defaultdict(int)
    for a, b in zip(name, yearning):
        data[a] = b
    for i in photo:
        answer.append(sum(map(lambda x : data[x],i)))     
    return answer
from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    data = defaultdict(int)
    for i in range(len(name)):
        data[name[i]] = yearning[i]
    for i in photo:
        total = 0
        for j in i:
            total += data[j]
        answer.append(total)    
    return answer
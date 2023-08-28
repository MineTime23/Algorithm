from collections import defaultdict

def solution(score):
    data = defaultdict(int)
    sorted_score = sorted(score, key = lambda x : -(x[0] + x[1])/2)
    for i,v in enumerate(sorted_score):
        if data[(v[0] + v[1])/2] == 0:
            data[(v[0] + v[1])/2] = i+1
    return [data[(i[0] + i[1])/2] for i in score]
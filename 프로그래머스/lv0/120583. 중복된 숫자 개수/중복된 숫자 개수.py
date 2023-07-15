from collections import defaultdict
def solution(array, n):
    data = defaultdict(int)
    for i in array:
        data[i] += 1
    return data[n]
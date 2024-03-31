import itertools

def solution(numbers):
    answer = []
    data = set()
    for i in itertools.combinations(numbers,2):
        data.add(sum(i))
    return sorted(list(data))
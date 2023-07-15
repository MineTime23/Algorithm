import itertools
def solution(numbers):
    a = set()
    for i in itertools.combinations(numbers,2):
        a.add(sum(i))
    return sorted(list(a))
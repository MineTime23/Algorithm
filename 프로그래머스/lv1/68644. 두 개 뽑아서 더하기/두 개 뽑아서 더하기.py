import itertools
def solution(numbers):
    result = set()
    for i in itertools.combinations(numbers,2):
        result.add(sum(i))
    return sorted(list(result))
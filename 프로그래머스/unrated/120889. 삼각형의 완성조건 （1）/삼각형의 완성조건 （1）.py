def solution(sides):
    sides.sort()
    return 1 if sum(sides)-sides[-1] > sides[-1] else 2
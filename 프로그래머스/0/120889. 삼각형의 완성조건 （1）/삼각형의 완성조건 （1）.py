def solution(sides):
    max_num = max(sides)
    return 1 if sum(sides) > 2 * max_num else 2
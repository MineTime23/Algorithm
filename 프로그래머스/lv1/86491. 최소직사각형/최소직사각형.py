def solution(sizes):
    max_num = 0
    min_num = 0
    for a,b in sizes:
        if max_num < max(a,b):
            max_num = max(a,b)
        if min_num < min(a,b):
            min_num = min(a,b)
    return max_num * min_num
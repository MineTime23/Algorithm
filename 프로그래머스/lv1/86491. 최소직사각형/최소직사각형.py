def solution(sizes):
    max_n = 0
    min_n = 0
    for a,b in sizes:
        if max(a,b) > max_n:
            max_n = max(a,b)
        if min(a,b) > min_n:
            min_n = min(a,b)
    return max_n * min_n
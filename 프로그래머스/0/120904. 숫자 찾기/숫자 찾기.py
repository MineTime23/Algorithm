def solution(num, k):
    for i,a in enumerate(str(num)):
        if int(a) == k:
            return i+1
    return -1
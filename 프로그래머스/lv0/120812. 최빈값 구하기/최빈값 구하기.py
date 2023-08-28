from collections import Counter

def solution(array):
    cnt = Counter(array)
    array2 = sorted(cnt.items(),key=lambda x : -x[1])
    if len(array2) == 1:
        return array2[0][0]
    elif array2[0][1] == array2[1][1]:
        return -1
    else:
        return array2[0][0]
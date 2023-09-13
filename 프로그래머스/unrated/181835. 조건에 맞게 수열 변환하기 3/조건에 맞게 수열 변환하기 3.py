def solution(arr, k):
    if k % 2 == 1:
        arr = list(map(lambda x : x * k,arr))
    else:
        arr = list(map(lambda x : x + k,arr))
    return arr
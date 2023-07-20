def solution(arr, k):
    if k%2 == 1:
        return list(map(lambda x : k * x,arr))
    else:
        return list(map(lambda x : k + x,arr))
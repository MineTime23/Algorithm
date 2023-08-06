def solution(arr, queries):
    for a,b in queries:
        for j in range(a,b+1):
            arr[j] += 1
    return arr
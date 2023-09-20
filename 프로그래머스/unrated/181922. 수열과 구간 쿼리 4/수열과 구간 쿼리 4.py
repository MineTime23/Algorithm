def solution(arr, queries):
    for a,b,k in queries:
        for i in range(a,b+1):
            if i % k == 0:
                arr[i] += 1
    return arr
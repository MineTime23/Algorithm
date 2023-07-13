def solution(arr, queries):
    answer = []
    for a,b,c in queries:
        arr1 = [arr[i] for i in range(a,b+1) if arr[i] > c]
        answer.append(min(arr1) if arr1 else -1)
    return answer
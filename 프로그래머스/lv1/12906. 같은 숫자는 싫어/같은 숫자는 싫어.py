
def solution(arr):
    result = []
    for i,v in enumerate(arr):
        if i == 0:
            result.append(v)
        elif arr[i-1] != arr[i] :
            result.append(v)
    return result
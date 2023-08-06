def solution(arr, idx):
    return -1 if not 1 in arr[idx:] else arr[idx:].index(1)+idx
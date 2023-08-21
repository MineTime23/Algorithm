def solution(arr):
    min_num = min(arr)
    result = [i for i in arr if i != min_num]
    return result if result else [-1]
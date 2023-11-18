def solution(array):
    max_data = max(array)
    return [max_data, array.index(max_data)]
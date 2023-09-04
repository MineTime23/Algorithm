def solution(array, n):
    array.sort()
    array = sorted(array, key = lambda x : (abs(x-n),-n))
    return array[0]
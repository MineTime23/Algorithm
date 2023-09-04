def solution(array, n):
    answer = []
    array.append(n)
    array.sort()
    idx = array.index(n)
    if idx-1 >= 0 and idx-1 < len(array):
        answer.append(array[idx-1])
    if idx+1 >= 0 and idx+1 < len(array):
        answer.append(array[idx+1])
    if len(answer) == 1:
        return answer[0]
    else:
        if abs(answer[0]-n) <= abs(answer[1]-n):
            return answer[0]
        else:
            return answer[1]
    return answer
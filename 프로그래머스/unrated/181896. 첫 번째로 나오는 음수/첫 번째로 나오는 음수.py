def solution(num_list):
    answer = -1
    for i,v in enumerate(num_list):
        if v < 0:
            return i
    return answer
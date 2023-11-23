def solution(num, k):
    answer = -1
    for i,v in enumerate(str(num)):
        if v == str(k):
            return i+1
    return answer
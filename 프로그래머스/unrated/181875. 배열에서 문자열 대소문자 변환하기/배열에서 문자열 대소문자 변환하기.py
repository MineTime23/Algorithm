def solution(strArr):
    answer = [v.lower() if i%2 == 0 else v.upper() for i,v in enumerate(strArr)]
    return answer
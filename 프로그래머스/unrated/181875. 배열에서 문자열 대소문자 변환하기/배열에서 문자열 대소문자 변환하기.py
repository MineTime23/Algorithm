def solution(strArr):
    return [item.lower() if i%2 == 0 else item.upper() for i,item in enumerate(strArr) ]
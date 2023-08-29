from collections import Counter
def solution(X, Y):
    common = Counter(X)&Counter(Y)
    if list(common.keys()) == 	['0']:
        return "0"
    if len(list(common.elements())) == 0:
        return "-1"
    result = ''.join(sorted(list(common.elements()),reverse=True))
    if result == "00":
        return "0"
    return result
from collections import Counter
def solution(strArr):
    strArr = list(map(lambda x : len(x),strArr))
    arrange = Counter(strArr)
    arrange = arrange.most_common()
    return arrange[0][1]
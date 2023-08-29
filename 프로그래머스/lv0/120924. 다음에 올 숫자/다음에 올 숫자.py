def solution(common):
    if len(common) >= 3:
        if common[2] - common[1] == common[1] - common[0]:
            return common[-1] + common[2] - common[1]
        else:
            return common[-1] * (common[2] // common[1])
    else:
        if int(common[1]/common[0]) == common[1]/common[0]:
            return common[-1] * (common[1] // common[0])
        else:
            return common[-1] + common[1] - common[0]
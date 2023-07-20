def solution(box, n):
    box = list(map(lambda x : x//n,box))
    return box[0] * box[1] * box[2]
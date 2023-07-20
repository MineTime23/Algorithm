def solution(box, n):
    box = list(map(lambda x : str(x//n),box))
    return int(eval('*'.join(box)))
def solution(box, n):
    return eval('*'.join(list(map(lambda x : str(x//n),box))))
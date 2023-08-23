def solution(n, control):
    dict1 = {"w":1,"s":-1,"d":10,"a":-10}
    return sum(map(lambda x : dict1[x],list(control))) + n
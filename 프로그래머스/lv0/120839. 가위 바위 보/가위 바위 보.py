def solution(rsp):
    data = {"2":"0","0":"5","5":"2"}
    return ''.join(map(lambda x : data[x],rsp))
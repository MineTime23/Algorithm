def solution(rsp):
    res = {"2": "0","0":"5","5":"2"}
    answer = ""
    for i in rsp:
        answer += res[i]
    return answer
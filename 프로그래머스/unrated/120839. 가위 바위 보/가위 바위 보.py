data = {"2" : "0", "0" : "5", "5" : "2"}

def solution(rsp):
    answer = ''
    for i in rsp:
        answer += data[i]
    return answer
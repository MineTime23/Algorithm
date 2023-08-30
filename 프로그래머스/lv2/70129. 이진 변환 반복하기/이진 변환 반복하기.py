def solution(s):
    answer = [0,0]
    while s != "1":
        answer[0] += 1
        a = len(s)
        s = s.replace("0","")
        answer[1] += a-len(s)
        s = bin(len(s))[2:]
    return answer
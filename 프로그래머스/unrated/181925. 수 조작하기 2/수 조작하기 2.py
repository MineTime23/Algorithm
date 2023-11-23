def solution(numLog):
    data = {1 : "w", -1 : "s", 10 : "d", -10 : "a"}
    answer = ''
    for i in range(1, len(numLog)):
        answer += data[numLog[i] - numLog[i-1]]
    return answer
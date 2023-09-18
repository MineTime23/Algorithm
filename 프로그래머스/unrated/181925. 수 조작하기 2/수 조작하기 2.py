def solution(numLog):
    data = {1:"w",-1:"s",10:"d",-10:"a"}
    res = [data[numLog[i] - numLog[i-1]] for i in range(1,len(numLog))]
    return ''.join(res)
def solution(n, m, section):
    answer = 0
    temp = [0] * (n+1)
    for i in section:
        temp[i] = 1
    for i in range(n+1):
        if temp[i] == 1:
            answer += 1
            for j in range(i,i+m):
                if j <= n:
                    temp[j] = 0
    return answer
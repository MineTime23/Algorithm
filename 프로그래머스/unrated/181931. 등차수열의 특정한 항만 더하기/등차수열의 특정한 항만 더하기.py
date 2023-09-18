def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        res = a + i*d
        if included[i]:
            answer += res
    return answer
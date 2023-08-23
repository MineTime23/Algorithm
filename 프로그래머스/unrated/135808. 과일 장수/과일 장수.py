def solution(k, m, score):
    score.sort(reverse=True)
    result = [score[i] for i in range(m-1,len(score),m)]
    return sum(result) * m
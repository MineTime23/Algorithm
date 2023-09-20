
def solution(sequence, k):
    answer = []
    i = 0
    j = 0
    sum_n = sequence[0]
    while True:
        a = sum_n
        if sum_n < k:
            j += 1
            if j > len(sequence)-1:
                break
            sum_n += sequence[j]
        elif sum_n > k:
            sum_n -= sequence[i]
            i += 1
            if i > len(sequence)-1:
                break
        elif sum_n == k:
            answer.append((i,j))
            sum_n -= sequence[i]
            i += 1
            if i > len(sequence)-1:
                break
        b = sum_n 
    answer = sorted(answer, key = lambda x : (x[1]-x[0], x[0]))
    return answer[0]
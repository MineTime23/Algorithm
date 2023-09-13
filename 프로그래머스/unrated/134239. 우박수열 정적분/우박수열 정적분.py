def solution(k, ranges):
    cnt = k
    answer = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
            answer.append(k)
        else:
            k = 3 * k + 1
            answer.append(k)
    answer = [(answer[i] + answer[i-1])/2 for i in range(1, len(answer))]
    cnt = len(answer)
    result = []
    for a,b in ranges:
        #print(a,cnt+b)
        if a > cnt + b:
            result.append(-1.0)
        else:
            result.append(sum(answer[a:cnt+b]))
    return result
def solution(num_list):
    res = []
    for i in num_list:
        
        answer = 0
        while i != 1:
            if i % 2 == 0:
                answer += 1
                i //= 2
            else:
                answer += 1
                i -= 1
                i //= 2
        res.append(answer)
    return sum(res)
def solution(answers):
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0,0,0,0]
    for i in range(len(answers)):
        if answers[i] == n1[i%5]:
            result[1] += 1
        if answers[i] == n2[i%8]:
            result[2] += 1
        if answers[i] == n3[i%10]:
            result[3] += 1
    answer = [i for i in range(len(result)) if result[i] == max(result)]
    return sorted(answer)
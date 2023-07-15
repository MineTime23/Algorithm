def solution(array, commands):
    answer = []
    for a,b,m in commands:
        answer.append(sorted(array[a-1:b])[m-1])
    return answer
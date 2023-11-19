def solution(age):
    answer = ''
    data = {}
    for i in range(0,27):
        data[str(i)] = chr(i+97)
    for i in str(age):
        answer += data[i]
    return answer
def solution(my_strings, parts):
    answer = ''
    for a, b in zip(my_strings,parts):
        answer += a[b[0]:b[1]+1]
    return answer
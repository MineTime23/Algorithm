from collections import defaultdict

def solution(my_string):
    answer = ''
    data = defaultdict(int)
    for i in my_string:
        if data[i] == 0:
            answer += i
            data[i] += 1
    return answer
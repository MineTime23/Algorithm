from collections import defaultdict
def solution(s):
    answer = 0
    temp = ""
    main = ""
    for i,v in enumerate(s):
        
        if temp == "":
            data = defaultdict(int)
        if i == 0 or temp == "":
            temp += v
            data[v] += 1
            main = v
        elif v == main:
            temp += v
            data[v] += 1
        elif v != main:
            temp += v
        if data[main] and len(temp) // data[main] == 2:
            answer += 1
            temp = ""
    return answer+1 if temp else answer
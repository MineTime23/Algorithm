from collections import defaultdict

def solution(record):
    answer = []
    data = defaultdict(list)
    for i in record:
        str1 = i.split()
        if str1[0] == "Enter" or str1[0] == "Change":
            if len(data[str1[1]]) == 0:
                data[str1[1]].append(str1[2])
            else:
                data[str1[1]][0] = str1[2]
    for i in record:
        str1 = i.split()
        if str1[0] == "Enter":
            answer.append(f"{data[str1[1]][0]}님이 들어왔습니다.")
        elif str1[0] == "Leave":
            answer.append(f"{data[str1[1]][0]}님이 나갔습니다.")
    
    return answer
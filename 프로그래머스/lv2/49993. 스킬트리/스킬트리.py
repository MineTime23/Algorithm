from collections import defaultdict

def solution(skill, skill_trees):
    answer = 0
    data = defaultdict(int)
    for i,v in enumerate(skill):
        data[v] = i+1
    
    for i in skill_trees:
        temp = []
        for  j in i:
            if data[j] != 0 and data[j] >= 1:
                if data[j] == 1:
                    temp.append(data[j])
                else:
                    if len(temp) == 0:
                        break
                    if temp[-1] != data[j]-1:
                        break
                    temp.append(data[j])
        else:
            answer += 1
    return answer
import re
def solution(dartResult):
    answer = 0
    current = 0
    data = {"S":1, "D" : 2, "T": 3}
    pattern = r'([SDT][#*]*)'
    result = re.split(pattern, dartResult)
    result = result[:-1]
    res = []
    #print(result)
    
    for i in result:
        if i.isnumeric():
            res.append(int(i))
        elif i in ["S","D","T"]:
            res[-1] = res[-1] ** data[i]
        elif len(i) == 2:
            res[-1] = res[-1] ** data[i[0]]
            if i[1] == "#":
                res[-1] *= (-1)
            elif i[1] == "*":
                if len(res) >= 2:
                    res[-1] *= 2
                    res[-2] *= 2
                else:
                    res[-1] *= 2

    return sum(res)
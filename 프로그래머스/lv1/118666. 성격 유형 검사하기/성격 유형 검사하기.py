from collections import defaultdict

def solution(survey, choices):
    answer = ''
    data = defaultdict(int)
    for i in range(len(survey)):
        if choices[i] >= 5:
            data[survey[i][1]] += abs(4-choices[i])
        else:
            data[survey[i][0]] += abs(4-choices[i])
    #print(data.items())
    if data['R'] >= data['T']:
        answer += "R"
    else:
        answer += "T"
    if data['C'] >= data['F']:
        answer += "C"
    else:
        answer += "F"   
    if data['J'] >= data['M']:
        answer += "J"
    else:
        answer += "M"
    if data['A'] >= data['N']:
        answer += "A"
    else:
        answer += "N"
    return answer
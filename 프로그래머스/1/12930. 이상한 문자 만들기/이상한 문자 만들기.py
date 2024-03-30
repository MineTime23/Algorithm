def solution(s):
    answer = ''
    
    s = s.lower()    
    flag = 0
    for i in range(len(s)):
        if s[i] == " ":
            flag = 0
            answer += s[i]
        elif flag%2 == 0:
            answer += s[i].upper()
            flag += 1
        else:
            answer += s[i]
            flag += 1
    return answer
def solution(s):
    s = s.lower()
    answer = ""
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
        elif s[i-1] == " " and s[i] != " ":
            answer += (s[i].upper())
        else:
            answer += s[i]
    return answer
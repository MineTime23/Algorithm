def solution(s):
    answer = ""
    s = s.lower()
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        elif i == 0 and s[i].isalpha():
            answer += s[i].upper()
        elif i != 0 and s[i-1] == " " and s[i].isalpha():
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer
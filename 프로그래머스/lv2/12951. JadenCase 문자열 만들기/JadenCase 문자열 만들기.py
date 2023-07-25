def solution(s):
    answer = ""
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        elif (i == 0) or (i != 0 and s[i-1] == " "):
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer

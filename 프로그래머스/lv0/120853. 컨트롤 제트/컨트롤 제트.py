def solution(s):
    answer = 0
    s = s.split()
    for i,v in enumerate(s):
        if (i != len(s)-1 and s[i+1] == "Z") or v == "Z":
            continue
        else:
            answer += int(v)
    return answer
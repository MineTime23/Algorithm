def solution(s):
    s = s.upper()
    a = 0
    b = 0
    for i in s:
        if i == "P":
            a += 1
        elif i == "Y":
            b += 1
    return True if a == b else False
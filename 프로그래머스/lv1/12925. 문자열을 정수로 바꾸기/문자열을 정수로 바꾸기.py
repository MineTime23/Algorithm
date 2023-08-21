def solution(s):
    return -int(s[1:]) if s.startswith("-") else int(s)
def solution(s):
    answer = []
    for i in s:
        if i == "(":
            answer.append("(")
        else:
            if answer and answer[-1] == "(":
                answer.pop()
            else:
                return False
    if answer:
        return False
    return True
def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True
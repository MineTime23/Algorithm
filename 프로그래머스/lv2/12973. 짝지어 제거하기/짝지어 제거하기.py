def solution(s):
    stack = []
    for i,v in enumerate(s):
        if i == 0:
            stack.append(v)
        elif stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    return 1 if not stack else 0
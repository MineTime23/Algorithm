def solution(arr):
    stack = []
    for i,v in enumerate(arr):
        if i == 0:
            stack.append(v)
        elif stack[-1] != v:
            stack.append(v)
    return stack
def judg(s):
    stack = []
    for i in s:
        if i == "[" or i == "{" or i == "(":
            stack.append(i)
        elif i == "]":
            if not stack:
                return False
            elif stack and stack[-1] != "[":
                return False
            elif stack and stack[-1] == "[":
                stack.pop()
        elif i == ")":
            if not stack:
                return False
            elif stack and stack[-1] != "(":
                return False 
            elif stack and stack[-1] == "(":
                stack.pop()
        elif i == "}":
            if not stack:
                return False
            elif stack and stack[-1] != "{":
                return False
            elif stack and stack[-1] == "{":
                stack.pop()
    if len(stack) != 0:
        return False
    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        if judg(s):
            answer += 1
        s = s[1:] + s[0]
    return answer
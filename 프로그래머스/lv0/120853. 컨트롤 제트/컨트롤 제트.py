def solution(s):
    answer = 0
    s =s.split()
    stack = []
    for i in s:
        if i == "Z":
            stack.pop()
        else:
            stack.append(int(i))
    return sum(stack)
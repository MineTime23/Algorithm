

def solution(arr):
    answer = []
    stack = []
    
    for i in arr:
        if not stack or stack[-1] != i:
            answer.append(i)
            stack.append(i)
    return answer
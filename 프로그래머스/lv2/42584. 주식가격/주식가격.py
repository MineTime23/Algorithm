def solution(prices):
    answer = [0] * len(prices)
    
    stack = []
    for i in range(len(prices)):
        
        while stack and prices[i] < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i-idx
        stack.append(i)  
    for i in range(len(answer)):
        if answer[i] == 0:
            answer[i] = len(answer)-i-1
    return answer
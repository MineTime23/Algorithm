def solution(food):
    answer = ''
    for i in range(1,len(food)):
        if food[i]%2 == 1:
            food[i] -= 1
        food[i] //= 2
        answer += f"{i}" * food[i]
        
    return answer + "0" + answer[::-1]
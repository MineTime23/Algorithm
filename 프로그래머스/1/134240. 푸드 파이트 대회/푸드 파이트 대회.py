def solution(food):
    answer = ''
    for i,v in enumerate(food):
        if i == 0:
            continue
        else:
            answer += (f"{i}" * (v//2)) 
    return answer + "0" + answer[::-1]
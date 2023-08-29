
def solution(s):
    answer = 0
    temp = ""
    temp_num = 0
    other_num = 0
    
    for i in range(len(s)):
        if i == 0 or temp_num == 0:
            temp = s[i]
            temp_num += 1
        elif s[i] == temp:
            temp_num += 1
        elif s[i] != temp:
            other_num  += 1
        
        if other_num == temp_num:
            answer += 1
            temp_num = 0
            other_num = 0
            
    if temp_num!= 0 or other_num != 0:
        return answer + 1
    return answer
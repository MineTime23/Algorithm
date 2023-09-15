def solution(ingredient):
    answer = 0
    str1 = ""
    for i in ingredient:
        str1 += str(i)
        if str1.endswith("1231"):
            answer += 1 
            str1 = str1[:-4]
    return answer
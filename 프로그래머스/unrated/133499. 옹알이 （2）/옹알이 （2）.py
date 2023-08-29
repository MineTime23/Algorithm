def solution(babbling):
    answer = 0
    for i in babbling:
        str1 = i.replace("aya","1").replace("ye","2").replace("woo","3").replace("ma","4")
        if str1.isdigit():
            if len(str1) == 1:
                answer += 1
            else:
                for i in ["11","22","33","44"]:
                    if i in str1:
                        break
                else:
                    answer += 1
    return answer
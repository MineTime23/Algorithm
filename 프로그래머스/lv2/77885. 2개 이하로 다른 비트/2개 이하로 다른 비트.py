def solution(numbers):
    answer = []
    for i in numbers:
        str1 = bin(i)[2:]
        if str1[-1] == "0":
            answer.append(i+1)
        elif "01" in str1:
            for i in range(len(str1)-1,1,-1):
                if str1[i] == "1" and str1[i-1] == "0":
                    idx = i-1
                    break
            result = int(str1[:idx] + str1[idx:].replace("01","10"),2)
            answer.append(result)
        else:
            result = int("10"+str1[1:],2)
            answer.append(result)
    return answer
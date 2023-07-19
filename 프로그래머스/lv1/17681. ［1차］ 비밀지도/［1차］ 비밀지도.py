def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(bin(arr1[i]|arr2[i])[2:])
        answer[-1] = answer[-1].replace("1","#")
        answer[-1] = answer[-1].replace("0"," ")
        if len(answer[-1]) < n:
            answer[-1] = " " * (n-len(answer[-1])) + answer[-1]
    return answer
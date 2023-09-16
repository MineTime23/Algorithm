def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1,arr2):
        res = bin(a|b)[2:]
        if len(res) < n:
            res = " " * (n - len(res)) + res
        res = res.replace("1","#")
        res = res.replace("0"," ")
        answer.append(res)
    return answer
def solution(myString, pat):
    answer = 0
    for i in range(0,len(myString)):
        if myString[i:].startswith(pat):
            answer += 1
    return answer
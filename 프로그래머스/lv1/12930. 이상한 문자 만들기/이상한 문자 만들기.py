def solution(s):
    answer = ''
    cnt = 0
    for i in s:
        if i == " ":
            cnt = 0
            answer += " "
        else:
            cnt += 1
            if cnt % 2 == 1:
                answer += i.upper()
            else:
                answer += i.lower()
    return answer
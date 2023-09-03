def convert(n,num):
    str1 = ""
    data = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
    if num == 1 or num == 0:
        return str(num)
    while num != 0:
        if num%n >= 10:
            str1 += data[num%n]
        else:
            str1 += str(num%n)
        num //= n
    return str1[::-1]

def solution(n, t, m, p):
    answer = ''
    cnt = 0
    while len(answer) < t*m:
        answer += convert(n,cnt)
        cnt += 1
    return answer[p-1:t*m:m]
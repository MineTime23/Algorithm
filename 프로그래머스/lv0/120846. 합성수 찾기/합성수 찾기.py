def cal(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if i == 1 or i == 2:
            continue
        else:
            if cal(i):
                continue
            else:
                answer += 1
    return answer
def solution(s):
    answer = 10000
    if len(s) == 1:
        return 1
    # 1개 단위로 잘랐을 때 부터 s의 길이개의 단위로 잘랐을 때
    for i in range(1, len(s)):
        cnt = len(s)
        temp = 1
        for j in range(0, len(s),i):
            if j == 0:
                continue
            elif s[j-i:j] == s[j:j+i]:
                cnt -= i
                temp  += 1
            elif s[j-i:j] != s[j:j+i]:
                if temp >= 2:
                    cnt += len(str(temp))
                    temp = 1
        if temp >= 2:
            cnt += len(str(temp))
        answer = min(answer,cnt)
    return answer
def solution(cards):
    cards = [0] + cards
    vol = [False] * (len(cards)+1)
    
    answer = []
    for i in range(1, len(cards)):
        if vol[i] == False:
            cnt = 0
            idx = i
            while vol[idx] == False:
                vol[idx] = True
                idx = cards[idx]
                cnt += 1
            answer.append(cnt)
    answer.sort() 
    if len(answer) == 1:
        return 0
    return answer[-1] * answer[-2]
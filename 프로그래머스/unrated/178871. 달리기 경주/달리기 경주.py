from collections import defaultdict
def solution(players, callings):
    data = defaultdict(int)
    for i in range(len(players)):
        data[players[i]] = i
    for i in callings:
        num = data[i]
        front = players[num-1]
        players[num], players[num-1] = players[num-1], players[num] 
        data[i] -= 1
        data[front] += 1
    return players
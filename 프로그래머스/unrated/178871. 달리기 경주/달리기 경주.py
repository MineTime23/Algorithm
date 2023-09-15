from collections import defaultdict

def solution(players, callings):
    answer = []
    idx_data = defaultdict(int)
    for i,v in enumerate(players):
        idx_data[v] = i
    #print(idx_data.items())
    for i in callings:
        idx = idx_data[i]
        idx_data[i] = idx-1
        idx_data[players[idx-1]] = idx
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players
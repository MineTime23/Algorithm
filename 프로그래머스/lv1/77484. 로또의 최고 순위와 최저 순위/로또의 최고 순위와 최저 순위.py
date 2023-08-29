def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    res = len(set(lottos)&set(win_nums))
    return [rank[res + lottos.count(0)],rank[res]]